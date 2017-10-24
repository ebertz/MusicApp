# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse
from models import Artist, Album, Song
# Create your views here.

def index(request):
    albumlist = Album.objects.all()
    return render(request, "music/index.html", { 'albumlist': albumlist})


class Album_View(generic.DetailView):
    model = Album
    template_name = "music/album.html"


class Artist_View(generic.DetailView):
    model = Artist
    template_name = "music/artist.html"