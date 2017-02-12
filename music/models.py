from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Album (models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)


class Song(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type = models.CharField(max_length=100)

    new = models.CharField(max_length=100)