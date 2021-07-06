import base64
import logging
import os

from django.shortcuts import redirect, render
from django.http import HttpResponse, FileResponse
from .quotemaker import quotemaker
from .quotemaker.colour_constants import colour_constants as colour
from .twitter import twitter

# Create your views here.
def index(request):
    quote_img = quotemaker.controlled(
        "Sweet Iced Coffee.ttf", colour.WHITE, colour.BLACK, 50, False
    )
    image_data = base64.b64encode(quote_img).decode("utf-8")
    context = {"image_data": image_data}
    return render(request, "index.html", context)


def tweet(request):
    image_data = request.POST["image_data"]
    image = base64.b64decode(image_data)
    with open("tweetpic.jpg", "wb") as f:
        f.write(image)
    twitter.api.update_with_media("tweetpic.jpg", twitter.tweet_text)
    os.remove("tweetpic.jpg")
    return redirect("index")
