from django.shortcuts import render

from collect_app.forms import GetNameAge


def getnameage (request):
    form = GetNameAge()
    return render(request, "index.html", {"form": form})
