from django.http import HttpResponse
from django.shortcuts import render
from .models import Image,Category



def welcome(request):
    return render(request,'welcome.html')

def all_photos(request):
    photos = Image.get_photos()
    return render(request,'all-photos/all-photos.html', {"photos":photos})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        Category = request.GET.get("image")
        searched_image = Image.search_by_category(Category)
        message = f"{Category}"

        return render(request, 'all-photos/search.html',{"message":message,"image": searched_image})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})
