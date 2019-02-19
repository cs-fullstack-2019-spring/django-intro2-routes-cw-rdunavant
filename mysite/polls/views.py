from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Here you go! Gray t shirts!")
    return HttpResponse("Sponge Bob FOREVER!")
