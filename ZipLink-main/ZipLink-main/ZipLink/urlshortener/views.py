from django.shortcuts import render, redirect
from django.urls import reverse

from . import service


def index(request):
    return render(request, 'urlshortener/index.html')


def redirect_hash(request, url_hash):
    original_url = service.load_url(url_hash).original_url
    return redirect(original_url)


def shorten_post(request):
    return shorten(request, request.POST['url'])


def shorten(request, url):
    shortened_url_hash = service.shorten(url)
    # shortened_url = request.build_absolute_uri(reverse('redirect', args=[shortened_url_hash]))
    shortened_url = request.build_absolute_uri(shortened_url_hash)

    print("\n\nshortened URL:",shortened_url)
    return render(request, 'urlshortener/link.html', {'shortened_url': shortened_url})