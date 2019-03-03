from django.http import HttpResponse
from django.shortcuts import render
from .models import Image,Category


def all_photos(request):
    images = Image.get_photos()
    return render(request,'all-photos.html', {"images":images})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        Category = request.GET.get("image")
        searched_images = Image.search_by_category(category)
        message = f"{category}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


# def location(request,location):
#         locations = Image.filter_by_location(location)
#         return render(request,'location.html',{"images": locations})