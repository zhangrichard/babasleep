from django.shortcuts import render

from .models import Album
# Create your views here.
from django.http import HttpResponse
from django.template import loader



def index(request):
    all_album  = Album.objects.all()

    template = loader.get_template('')
    html = ""
    for album in all_album:
        url = '/music/'+str(album.id)+'/'
        html += '<a href="' + url + '">' + album.album_title + '</a><br>'

    return HttpResponse(html)

def detail(request,album_id):
    return HttpResponse("<h2> Detail for Album id: "+str(album_id)+"</h2>")