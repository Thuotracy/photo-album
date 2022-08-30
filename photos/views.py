from email.mime import image
from unicodedata import category
from django.shortcuts import render
from .models import Category, Photo

# Create your views here.

def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()

    context = {'categories' : categories, 'photos' : photos}
    return render(request, 'photos/gallery.html', context)


def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photo': photo})


def addPhoto(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category =Category.object.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_created(name=data['category_new'])   
        else:
            category = None

        photo = Photo.objects.create(
            category=category,
            description=data['description'],
            image=image,
        )    

    context = {'categories' : categories}
    return render(request, 'photos/add.html', context)        