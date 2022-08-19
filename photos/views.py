from django.shortcuts import render

# Create your views here.

def gallery(request):
    return render(request, 'photos/gallery.html')

def viewPhoto(request, pk):
    return render(request, 'photos/photo.html')

def addPhoto(request):
    return render(request, 'photos/add.html')        