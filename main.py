import csv
import random
import time

import requests

from PIL import Image, ImageFont, ImageDraw


def get_image(w: int, h: int):
    response = requests.get(f"https://source.unsplash.com/random/{w}x{h}")
    if response.status_code == 200:
        filename = f"{time.time()}.jpg"
        with open(filename, "wb") as imagefile:
            for chunk in response:
                imagefile.write(chunk)
        return filename
    else:
        return None


def get_quote():
    with open("quotes_all.csv", "r") as quotes_csv:
        quotes = list(csv.reader(quotes_csv, delimiter=";"))[2:]
        index = random.randint(0, len(quotes))
        return quotes[index][0]


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


def draw_text(filename: str, image_text: list[str]):
    image = Image.open(filename)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("fonts/Risalah Cinta.otf", 60)
    for index, line in enumerate(image_text):
        draw.text((50, 50 * (index + 1)), line, (0, 0, 0), font=font)
        draw.text((48, (50 * (index + 1)) - 2), line, (240, 230, 140), font=font)
    draw.text((400, 500), "- Michael Scott", (0, 0, 0), font=font)
    draw.text((398, 498), "- Michael Scott", (240, 230, 140), font=font)
    image.save(filename)
    return None


def main():
    filename = get_image(800, 600)
    if not filename:
        print("Error getting image from Unsplash!")
        quit()

    quote = get_quote()
    if not quote:
        print("Error getting quote from quotes.rest!")
        quit()

    split_quote = block_quote(quote, 35)
    draw_text(filename, split_quote)

    return None


if __name__ == "__main__":
    for x in range(40):
        time.sleep(0.5)
        main()
