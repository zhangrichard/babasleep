from django.shortcuts import render
from django.http import Http404
from .models import Album
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views import generic


from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .form import UserForm


def index(request):
    all_albums = Album.objects.all()

    template = loader.get_template('music/index.html')
    context = {
        'all_albums': all_albums,
    }

    return render(request,"music/index.html",context)


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = "all_albums"
    def get_queryset(self):
        return Album.objects.all()



def detail(request, album_id):

    try:
        album = Album.objects.get(pk=album_id)

    except Album.DoesNotExist:
        raise Http404(" album doesn't exist ")

    return render(request, "music/detail.html", {'album': album})


class UserFormView(View):
    form_class = UserForm
    template_name = "music/registration_form.html"

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user.username =
