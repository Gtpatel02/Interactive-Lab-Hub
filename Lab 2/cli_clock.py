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
# BUTTON
# ============================================================

# Button connected between GPIO 23 and GND

button = digitalio.DigitalInOut(board.D23)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP


# ============================================================
# IMAGE FOLDER
# ============================================================

IMAGE_FOLDER = "images"


# ============================================================
# FONT
# ============================================================

font = ImageFont.truetype(
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    16
)


# ============================================================
# ANIMATIONS
# ============================================================

# Each entry represents one scene/time period.
#
# p1 = 8 AM
# p2 = 9 AM
# p3 = 10 AM
# etc.
#
# For now, only add animations that actually exist.

animations = [

    # Animation 0 - 8 AM
    [
        "p1f1.png",
        "p1f2.png",
        "p1f3.png",
        "p1f4.png",
        "p1f5.png",
    ],

    # When you make the 9 AM animation, uncomment this:
    #
    # [
    #     "p2f1.jpg",
    #     "p2f2.jpg",
    #     "p2f3.jpg",
    #     "p2f4.jpg",
    #     "p2f5.jpg",
    # ],

]


# ============================================================
# LOAD IMAGE
# ============================================================

def load_image(filename):

    filepath = os.path.join(IMAGE_FOLDER, filename)

    print("Loading:", filepath)

    image = Image.open(filepath).convert("RGB")

    image_ratio = image.width / image.height
    screen_ratio = width / height

    # Resize image while preserving aspect ratio
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
# ADD CLOCK TO FRAME
# ============================================================

def add_clock(background):

    image = background.copy()

    draw = ImageDraw.Draw(image)

    current_time = time.strftime("%I:%M:%S %p")

    bbox = draw.textbbox(
        (0, 0),
        current_time,
        font=font
    )

    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    text_x = (width - text_width) // 2
    text_y = height - text_height - 12

    padding = 5

    # Black background behind time
    draw.rectangle(
        (
            text_x - padding,
            text_y - padding,
            text_x + text_width + padding,
            text_y + text_height + padding
        ),
        fill=(0, 0, 0)
    )

    # White time text
    draw.text(
        (text_x, text_y),
        current_time,
        font=font,
        fill=(255, 255, 255)
    )

    return image


# ============================================================
# PRELOAD ALL ANIMATIONS
# ============================================================

# Load everything into memory first.
# This prevents JPG loading from slowing down the animation.

loaded_animations = []

for animation in animations:

    loaded_frames = []

    for filename in animation:

        frame = load_image(filename)

        loaded_frames.append(frame)

    loaded_animations.append(loaded_frames)


print()
print("Animations loaded:", len(loaded_animations))
print("Press button to switch animation.")
print()


# ============================================================
# ANIMATION SETTINGS
# ============================================================

# Smaller number = faster animation
#
# 0.15 = about 6.7 FPS
# 0.10 = about 10 FPS

FRAME_DELAY = 0.15


# Start with first animation
current_animation = 0

# Start with first frame
current_frame = 0

# Used to detect a NEW button press
last_button_state = True


# ============================================================
# MAIN LOOP
# ============================================================

while True:

    # --------------------------------------------------------
    # CHECK BUTTON
    # --------------------------------------------------------

    button_state = button.value

    # Button uses pull-up:
    #
    # True  = not pressed
    # False = pressed

    if last_button_state and not button_state:

        # Move to next animation
        current_animation += 1

        # If we reach the end, return to animation 0
        if current_animation >= len(loaded_animations):
            current_animation = 0

        # Start new animation at frame 1
        current_frame = 0

        print(
            "Switched to animation:",
            current_animation + 1
        )

    last_button_state = button_state


    # --------------------------------------------------------
    # GET CURRENT ANIMATION
    # --------------------------------------------------------

    animation = loaded_animations[current_animation]


    # --------------------------------------------------------
    # GET CURRENT FRAME
    # --------------------------------------------------------

    background = animation[current_frame]


    # --------------------------------------------------------
    # ADD LIVE CLOCK
    # --------------------------------------------------------

    image = add_clock(background)


    # --------------------------------------------------------
    # DISPLAY FRAME
    # --------------------------------------------------------

    disp.image(image)


    # --------------------------------------------------------
    # MOVE TO NEXT FRAME
    # --------------------------------------------------------

    current_frame += 1

    if current_frame >= len(animation):
        current_frame = 0


    # --------------------------------------------------------
    # ANIMATION SPEED
    # --------------------------------------------------------

    time.sleep(FRAME_DELAY)
