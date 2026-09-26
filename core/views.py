from django.shortcuts import render

from . import content


def index(request):
    return render(request, "core/index.html", {"site": content.SITE})


def page_not_found(request, exception):
    return render(request, "core/404.html", {"site": content.SITE}, status=404)
