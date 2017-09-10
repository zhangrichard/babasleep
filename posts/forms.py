from django import forms

from .models import Post

from registration.forms import RegistrationForm

from django.conf import settings



class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields = ["title","content","image"]


            # class SignUpForm(forms.ModelForm):
#     class Meta:
#         model = settings.AUTH_USER_MODEL
#         fields = ["username"]