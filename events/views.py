from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def yellow_flowers(request: HttpRequest) -> HttpResponse:
    name = request.GET.get("name", "")
    return render(request, "flowers/yellow_flowers.html", {"name": name})


def valentine_v1(request: HttpRequest) -> HttpResponse:
    name = request.GET.get("name", "")
    return render(request, "valentine/v1.html", {"name": name})


def flower_garden(request: HttpRequest) -> HttpResponse:
    return render(request, "flowers/flower_garden.html")
