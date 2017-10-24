# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=200)
    bio = models.CharField(max_length=1000)

    def __str__(self):
        return name

class Album(models.Model):
    title = models.CharField(max_length= 200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    artwork = models.CharField(max_length=1000)

    def __str__(self):
        return title



class Song(models.Model):
    title = models.CharField(max_length= 200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return title