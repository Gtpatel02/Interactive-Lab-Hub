import time
import os
import digitalio
import board

from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789


# ============================================================
# DISPLAY SETUP
# ============================================================

cs_pin = digitalio.DigitalInOut(board.D5)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = digitalio.DigitalInOut(board.D24)

BAUDRATE = 24000000

spi = board.SPI()

disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)


# ============================================================
# SCREEN SIZE
# ============================================================

if disp.rotation % 180 == 90:
    height = disp.width
    width = disp.height
else:
    width = disp.width
    height = disp.height


# ============================================================
# BACKLIGHT
# ============================================================

backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True


# ============================================================
# SETTINGS
# ============================================================

IMAGE_FOLDER = "images"

# 0.15 seconds between frames
# Lower = faster animation
FRAME_DELAY = 0.15

# Number of animation frames per scene
FRAMES_PER_ANIMATION = 5


# ============================================================
# FONT
# ============================================================

font = ImageFont.truetype(
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    16
)


# ============================================================
# HOUR -> ANIMATION NUMBER
# ============================================================
#
# p1  = 8 AM
# p2  = 9 AM
# p3  = 10 AM
# ...
# p16 = 11 PM
# p17 = 12 AM
# p18 = 1 AM
# p19 = sleeping (2 AM - 7 AM)
#
# ============================================================

hour_to_animation = {
    8: 1,
    9: 2,
    10: 3,
    11: 4,
    12: 5,
    13: 6,
    14: 7,
    15: 8,
    16: 9,
    17: 10,
    18: 11,
    19: 12,
    20: 13,
    21: 14,
    22: 15,
    23: 16,

    0: 17,
    1: 18,

    # Same sleeping animation from 2 AM through 7:59 AM
    2: 19,
    3: 19,
    4: 19,
    5: 19,
    6: 19,
    7: 19,
}


# ============================================================
# LOAD IMAGE
# ============================================================

def load_image(filename):

    filepath = os.path.join(IMAGE_FOLDER, filename)

    print("Loading:", filepath)

    image = Image.open(filepath).convert("RGB")

    image_ratio = image.width / image.height
    screen_ratio = width / height

    # Resize while keeping aspect ratio
    if screen_ratio < image_ratio:
        scaled_width = image.width * height // image.height
        scaled_height = height
    else:
        scaled_width = width
        scaled_height = image.height * width // image.width

    image = image.resize(
        (scaled_width, scaled_height),
        Image.BICUBIC
    )

    # Center crop
    x = scaled_width // 2 - width // 2
    y = scaled_height // 2 - height // 2

    image = image.crop(
        (
            x,
            y,
            x + width,
            y + height
        )
    )

    return image


# ============================================================
# ADD CLOCK TO IMAGE
# ============================================================
def add_clock(background):

    image = background.copy()

    draw = ImageDraw.Draw(image)

    # Example:
    # 08:42:16 AM
    current_time = time.strftime("%I:%M:%S %p")

    bbox = draw.textbbox(
        (0, 0),
        current_time,
        font=font
    )

    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Center horizontally
    text_x = (width - text_width) // 2

    # Near bottom of screen
    text_y = height - text_height - 12

    # Draw time directly onto image in RED
    # No black background
    draw.text(
        (text_x, text_y),
        current_time,
        font=font,
        fill=(255, 0, 0)
    )

    return image


# ============================================================
# LOAD ALL 19 ANIMATIONS
# ============================================================
#
# Automatically generates:
#
# p1f1.png
# p1f2.png
# ...
# p19f5.png
#
# ============================================================

print()
print("Loading animation frames...")
print()

loaded_animations = {}


for animation_number in range(1, 20):

    loaded_animations[animation_number] = []

    for frame_number in range(1, FRAMES_PER_ANIMATION + 1):

        # Example:
        # animation 1, frame 3 -> p1f3.png

        filename = (
            f"p{animation_number}"
            f"f{frame_number}.png"
        )

        frame = load_image(filename)

        loaded_animations[animation_number].append(frame)


print()
print("All animations loaded!")
print()


# ============================================================
# MAIN CLOCK
# ============================================================

current_hour = None
current_frame = 0


while True:

    # --------------------------------------------------------
    # GET CURRENT HOUR
    # --------------------------------------------------------

    hour = int(time.strftime("%H"))


    # --------------------------------------------------------
    # CHECK FOR HOUR CHANGE
    # --------------------------------------------------------

    if hour != current_hour:

        current_hour = hour

        # Restart animation at frame 1
        current_frame = 0

        animation_number = hour_to_animation[hour]

        print()
        print("Current hour:", hour)
        print("Using animation: p" + str(animation_number))
        print()


    # --------------------------------------------------------
    # FIND CORRECT ANIMATION
    # --------------------------------------------------------

    animation_number = hour_to_animation[hour]

    animation = loaded_animations[animation_number]


    # --------------------------------------------------------
    # GET CURRENT FRAME
    # --------------------------------------------------------

    background = animation[current_frame]


    # --------------------------------------------------------
    # ADD CURRENT TIME
    # --------------------------------------------------------

    image = add_clock(background)


    # --------------------------------------------------------
    # DISPLAY IT
    # --------------------------------------------------------

    disp.image(image)


    # --------------------------------------------------------
    # MOVE TO NEXT FRAME
    # --------------------------------------------------------

    current_frame += 1

    if current_frame >= len(animation):
        current_frame = 0


    # --------------------------------------------------------
    # CONTROL ANIMATION SPEED
    # --------------------------------------------------------

    time.sleep(FRAME_DELAY)
