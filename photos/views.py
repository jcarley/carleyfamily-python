from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
from .models import Photo


class PhotoListView(ListView):
    model = Photo
    template_name = "photo_list.html"
