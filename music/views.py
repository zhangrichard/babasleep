from django.shortcuts import render
from django.http import Http404
from .models import Album
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def index(request):
    all_albums = Album.objects.all()

    template = loader.get_template('music/index.html')
    context = {
        'all_albums': all_albums,
    }

    return render(request,"music/index.html",context)


def detail(request, album_id):

    try:
        album = Album.objects.get(pk=album_id)

    except Album.DoesNotExist:
        raise Http404(" album doesn't exist ")

    return render(request, "music/detail.html", {'album': album})