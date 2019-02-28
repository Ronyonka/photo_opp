from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def all_photos(request):
    return render(request,'all-photos/all-photos.html')
