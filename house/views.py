from django.shortcuts import render
from django.http import HttpResponse


def note(request):
    return HttpResponse("Hello Django")

