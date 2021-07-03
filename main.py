import csv
import logging
import os
import random
import time

import requests

from io import BytesIO
from PIL import Image, ImageFont, ImageDraw
from typing import Tuple


logger = logging.getLogger(__name__)


class Font:
    font_file: str
    font_colour: Tuple[int, int, int]
    font_shadow: Tuple[int, int, int]
    font_size: int

    def __init__(
        self,
        font_file: str,
        font_colour: Tuple[int, int, int],
        font_shadow: Tuple[int, int, int],
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
        with open("quotes_all.csv", "r") as quotes_csv:
            quotes = list(csv.reader(quotes_csv, delimiter=";"))[2:]
            index = random.randint(0, len(quotes))
            return quotes[index][0]
    except FileNotFoundError:
        logging.error("Cannot find 'quotes_all.csv' file!\nExiting...")
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


def draw_text(image_bytes: bytes, font_data: Font, image_text: list[str]):
    image_object = BytesIO(image_bytes)
    filename = f"{time.time()}.jpg"

    image = Image.open(image_object)
    draw = ImageDraw.Draw(image)
    try:
        font = ImageFont.truetype(f"fonts/{font_data.font_file}", font_data.font_size)
    except OSError:
        logging.error(
            f"Cannot find font '{font_data.font_file}'! Did you put it in the 'fonts' directory?"
        )
        quit()

    for index, line in enumerate(image_text):
        draw.text((50, 50 * (index + 1)), line, font_data.font_shadow, font=font)
        draw.text((48, (50 * (index + 1)) - 2), line, font_data.font_colour, font=font)
    draw.text((400, 500), "- Michael Scott", font_data.font_shadow, font=font)
    draw.text((398, 498), "- Michael Scott", font_data.font_colour, font=font)
    image.save(filename)
    return None


def main():
    image_bytes = get_image(800, 600)
    if not image_bytes:
        print("Error getting image from Unsplash!")
        quit()

    quote = get_quote()
    if not quote:
        print("Error getting quote from quotes_all.csv!")
        quit()

    split_quote = block_quote(quote, 35)
    font_file = random.choice(os.listdir("fonts"))
    colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    shadow = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    font = Font(font_file, colour, shadow, 30)
    draw_text(image_bytes, font, split_quote)

    return None


if __name__ == "__main__":
    main()
