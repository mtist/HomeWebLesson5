from django.shortcuts import render
from .models import Page


def home(request):
    return render(request, 'home.html', {})


def pages(request, slug):
    page = Page.objects.get(slug=slug)
    return render(request, 'page.html', {'page': page})
