from django.shortcuts import render

from collect_app.forms import GetNameAge 

import logging 
from user_agents import parse


logger = logging.getLogger(__name__) # get an instance of a logger


def getnameage (request):
    form = GetNameAge()

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    browserstring = request.META['HTTP_USER_AGENT']
    user_agent = parse(browserstring)

    print(user_agent.browser.family)




    return render(request, "index.html", {"form": form})


def confirm (request):
    info = {
        "age": request.GET["age"], 
        "name" : request.GET["fname"]
        }
    return render(request, "confirm.html", info)