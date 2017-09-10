from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect,Http404
# Create your views here.
from django.contrib import messages
from .models import Post
from django.contrib.auth.models import User
from .forms import PostForm

def index(request):
    title = "welcome"
    # if request.user.is_authenticated():
    #
    #     title = "my title  %s"% (request.user)
    form = PostForm(request.POST or None, request.FILES or None)
    context = {
        "title":title,
        "form":form

    }
    return render(request,"home.html",context)



def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    if not request.user.is_authenticated():
        raise  Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        # messages.suceess(request,"Sucessful created")
        return HttpResponseRedirect(instance.get_absolute_url())
    # if request.method == "POST":
    #     print request.POST.get("content")
    else :
        messages.error(request,"not Sucessful created")
    context = {
        "form":form,

    }
    return render(request, "post_form.html",context)

def post_detail(request,id=None):
    instance = get_object_or_404(Post,id=id)
    context = {
        "title": instance.title,
        "instance":instance
    }
    return render(request, "post_detail.html",context)


def post_list(request):

    queryset = Post.objects.all().filter(user=request.user)
    userset =User.objects.all()
    print userset
    context_object_name = 'posts'
    if request.user.is_authenticated():
        context = {
            "object_list":userset,
            "title": "user Login in",
        }
    else :

        context = {
            "object_list": queryset,
            "title": "List",
        }
    return render(request, "post_list.html",context)


def post_update(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None,instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,"sucessfully saved")

        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.title,
        "instance": instance,
        'form': form
    }
    return render(request, "post_form.html", context)


def post_delete(request,id):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    return redirect("posts:list")
