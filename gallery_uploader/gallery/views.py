from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .models import image

class SubmitImage(CreateView):
    template_name = "gallery/create_image.html"
    model = image
    fields = "__all__"
    success_url = "/upload"

class imageView(ListView):
    model = image
    template_name = "gallery/images.html"
    context_object_name = "images"