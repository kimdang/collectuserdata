from django.shortcuts import render

from collect_app.forms import GetNameAge 

import logging 


logger = logging.getLogger(__name__) # get an instance of a logger


def getnameage (request):
    form = GetNameAge()
    return render(request, "index.html", {"form": form})


def confirm (request):
    info = {
        "age": request.GET["age"], 
        "name" : request.GET["fname"]
        }
    return render(request, "confirm.html", info)