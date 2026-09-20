# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

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

# Set up SPI
spi = board.SPI()

# Create the display
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
# IMAGE FOR EACH HOUR
# ============================================================

hour_images = {

    # Morning
    8:  "01_08AM_Waking_Up_320x240.jpg",
    9:  "02_09AM_Brushing_Teeth_320x240.jpg",
    10: "03_10AM_Eating_Breakfast_320x240.jpg",
    11: "04_11AM_Going_to_Class_320x240.jpg",

    # Afternoon
    12: "05_12PM_Sitting_on_a_Building_320x240.jpg",
    13: "06_01PM_Eating_Lunch_320x240.jpg",
    14: "07_02PM_MidDay_Swing_320x240.jpg",
    15: "08_03PM_Gym_320x240.jpg",
    16: "09_04PM_Walking_Grandma_320x240.jpg",
    17: "10_05PM_With_Chloe_320x240.jpg",

    # Evening
    18: "11_06PM_Getting_Pizza_320x240.jpg",
    19: "12_07PM_Getting_Chai_320x240.jpg",
    20: "13_08PM_Doing_Homework_320x240.jpg",
    21: "14_09PM_Stopping_a_Villain_320x240.jpg",
    22: "15_10PM_With_Grandfather_320x240.jpg",
    23: "16_11PM_Visiting_a_Memorial_320x240.jpg",

    # Midnight / early morning
    0: "17_12AM_Hanging_Upside_Down_320x240.jpg",
    1: "18_01AM_Getting_into_Bed_320x240.jpg",

    # Sleeping from 2 AM through 7:59 AM
    2: "19_02AM-07AM_Sleeping_320x240.jpg",
    3: "19_02AM-07AM_Sleeping_320x240.jpg",
    4: "19_02AM-07AM_Sleeping_320x240.jpg",
    5: "19_02AM-07AM_Sleeping_320x240.jpg",
    6: "19_02AM-07AM_Sleeping_320x240.jpg",
    7: "19_02AM-07AM_Sleeping_320x240.jpg",
}


# ============================================================
# LOAD IMAGE
# ============================================================

def load_image(filename):

    # Create path such as:
    # images/01_08AM_Waking_Up_320x240.jpg
    filepath = os.path.join(IMAGE_FOLDER, filename)

    print("Loading:", filepath)

    # Open image
    image = Image.open(filepath).convert("RGB")

    # Calculate image and screen aspect ratios
    image_ratio = image.width / image.height
    screen_ratio = width / height

    # Resize while maintaining aspect ratio
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

    # Crop and center the image
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
# MAIN CLOCK
# ============================================================

current_hour = None
background_image = None

while True:

    # --------------------------------------------------------
    # GET CURRENT HOUR
    # --------------------------------------------------------

    # %H gives us the hour from 0-23
    hour = int(time.strftime("%H"))


    # --------------------------------------------------------
    # CHANGE PICTURE WHEN THE HOUR CHANGES
    # --------------------------------------------------------

    if hour != current_hour:

        current_hour = hour

        # Find the image for this hour
        filename = hour_images[hour]

        print("Current hour:", hour)
        print("Changing image to:", filename)

        # Load new background image
        background_image = load_image(filename)


    # --------------------------------------------------------
    # COPY THE BACKGROUND
    # --------------------------------------------------------

    # We copy it so drawing the time does not permanently
    # modify our original background image.

    image = background_image.copy()

    draw = ImageDraw.Draw(image)


    # --------------------------------------------------------
    # GET CURRENT TIME
    # --------------------------------------------------------

    # Example:
    # 04:25:31 PM

    current_time = time.strftime("%I:%M:%S %p")


    # --------------------------------------------------------
    # CALCULATE SIZE OF TIME TEXT
    # --------------------------------------------------------

    bbox = draw.textbbox(
        (0, 0),
        current_time,
        font=font
    )

    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]


    # --------------------------------------------------------
    # POSITION TIME
    # --------------------------------------------------------

    # Center horizontally
    text_x = (width - text_width) // 2

    # Put it near the bottom
    text_y = height - text_height - 12


    # --------------------------------------------------------
    # DRAW BLACK BOX BEHIND TIME
    # --------------------------------------------------------

    padding = 5

    draw.rectangle(
        (
            text_x - padding,
            text_y - padding,
            text_x + text_width + padding,
            text_y + text_height + padding
        ),
        fill=(0, 0, 0)
    )


    # --------------------------------------------------------
    # DRAW CURRENT TIME
    # --------------------------------------------------------

    draw.text(
        (text_x, text_y),
        current_time,
        font=font,
        fill=(255, 255, 255)
    )


    # --------------------------------------------------------
    # DISPLAY IMAGE + TIME
    # --------------------------------------------------------

    disp.image(image)


    # --------------------------------------------------------
    # UPDATE EVERY SECOND
    # --------------------------------------------------------

    time.sleep(1)
