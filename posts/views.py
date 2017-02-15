from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Post
def index(request):

    render(request,HttpResponse("<h1> hello"))

def post_create(request):
    context = {
        "title": "List"
    }
    return render(request, "index.html",context)

def post_detail(request):
    context = {
        "title": "Detail"
    }
    return render(request, "index.html",context)


def post_list(request):

    queryset = Post.objects.all()

    context_object_name = 'posts'
    if request.user.is_authenticated():
        context = {
            "object_list":queryset,
            "title": "user Login in",
        }
    else :

        context = {
            "object_list": queryset,
            "title": "List",
        }
    return render(request, "index.html",context)


def post_update(request):
    render(request, HttpResponse("hello"))



def post_delete(request):
    render(request, HttpResponse("hello"))
