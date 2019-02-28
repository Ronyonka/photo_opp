from django.http import HttpResponse
from django.shortcuts import render
from .models import Image


# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def all_photos(request):
    photos = Image.get_photos()
    return render(request,'all-photos/all-photos.html', {"photos":photos})
