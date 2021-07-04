import csv
import logging
import os
import random
import time
import requests


from .colour_constants import colour_constants as colour
from io import BytesIO
from PIL import Image, ImageFont, ImageDraw
from typing import List


logger = logging.getLogger(__name__)


class Font:
    font_file: str
    font_colour: colour.RGB
    font_shadow: colour.RGB
    font_size: int

    def __init__(
        self,
        font_file: str,
        font_colour: colour.RGB,
        font_shadow: colour.RGB,
        font_size: int,
    ) -> None:
        self.font_file = font_file
        self.font_colour = font_colour
        self.font_shadow = font_shadow
        self.font_size = font_size


def get_image(w: int, h: int):
    response = requests.get(f"https://source.unsplash.com/random/{w}x{h}")
    if response.status_code == 200:
        return response.content
    else:
        logging.error(
            f"Error getting image from Unisplash! Response: ({response.status_code})"
        )
        response.raise_for_status()
        quit()


def get_quote():
    try:
        logging.error(os.listdir("."))
        with open("quotesite/quotemaker/quotes_all.csv", "r") as quotes_csv:
            quotes = list(csv.reader(quotes_csv, delimiter=";"))[2:]
            index = random.randint(0, len(quotes))
            return quotes[index]
    except FileNotFoundError:
        logging.error("Cannot find 'quotes_all.csv' file!\nExiting...")
        quit()


def get_shitpost():
    try:
        with open("./shitposts.csv", "r") as quotes_csv:
            quotes = list(csv.reader(quotes_csv, delimiter=";"))
            index = random.randint(0, len(quotes))
            return quotes[index][0]
    except FileNotFoundError:
        logging.error("Cannot find 'shitposts.csv' file!\nExiting...")
        quit()


def block_quote(quote: str, line_length: int):
    word_list = quote.split(" ")
    lines = []
    buffer = ""
    for index, word in enumerate(word_list):
        if (index + 1) == len(word_list):
            buffer += f"{word}"
            lines.append(buffer)
        elif (len(buffer) + len(word)) < line_length:
            buffer += f"{word} "
        else:
            lines.append(buffer)
            buffer = f"{word} "
    return lines


def draw_text(
    image_bytes: bytes,
    font_data: Font,
    image_text: List[str],
    author: str = "Michael Scott",
):
    # Unpack the colour.RGB into a tuple so they can work
    # with PIL ImageDraw RGB values
    font_colour = (
        font_data.font_colour.red,
        font_data.font_colour.green,
        font_data.font_colour.blue,
    )
    font_shadow = (
        font_data.font_shadow.red,
        font_data.font_shadow.green,
        font_data.font_shadow.blue,
    )

    # Parse the image bytes into a BytesIO object
    image_object = BytesIO(image_bytes)
    image = Image.open(image_object)
    draw = ImageDraw.Draw(image)

    # Try to load the font file
    try:
        font = ImageFont.truetype(
            f"quotesite/quotemaker/fonts/{font_data.font_file}", font_data.font_size
        )
    except OSError:
        logging.error(
            f"Cannot find font '{font_data.font_file}'! Did you put it in the 'fonts' directory?"
        )
        quit()

    # Draw the main body of text line by line
    for index, line in enumerate(image_text):
        draw.text((50, 50 * (index + 1)), line, font_shadow, font=font)
        draw.text((48, (50 * (index + 1)) - 2), line, font_colour, font=font)

    # Draw the author name in the bottom right corner
    draw.text((500, 500), f"- {author}", font_shadow, font=font)
    draw.text((498, 498), f"- {author}", font_colour, font=font)

    buf = BytesIO()
    image.save(buf, format="JPEG")
    return buf.getvalue()


def randomizer():
    image_bytes = get_image(800, 600)

    quote = get_quote()

    split_quote = block_quote(quote, 35)
    font_file = random.choice(os.listdir("fonts"))
    font_colour = colour.RGB(
        random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    )
    font_shadow = colour.RGB(
        random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    )
    font = Font(font_file, font_colour, font_shadow, 40)
    draw_text(image_bytes, font, split_quote)

    return None


def controlled(
    font_file: str,
    font_colour: colour.RGB,
    font_shadow: colour.RGB,
    font_size: int,
    show_author: bool = False,
):
    image_bytes = get_image(800, 600)
    quote = get_quote()
    split_quote = block_quote(quote[0], 35)
    font = Font(font_file, font_colour, font_shadow, font_size)
    if show_author:
        image = draw_text(image_bytes, font, split_quote, author=quote[1])
    else:
        image = draw_text(image_bytes, font, split_quote)

    return image


if __name__ == "__main__":
    controlled("Sweet Iced Coffee.ttf", colour.WHITE, colour.BLACK, 50, False)
