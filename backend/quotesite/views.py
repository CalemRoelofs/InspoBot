import base64

from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from .quotemaker import quotemaker
from .quotemaker.colour_constants import colour_constants as colour


# Create your views here.
def index(request):
    quote_img = quotemaker.controlled(
        "Sweet Iced Coffee.ttf", colour.WHITE, colour.BLACK, 50, False
    )
    image_data = base64.b64encode(quote_img).decode("utf-8")
    context = {"image_data": image_data}
    return render(request, "index.html", context)
