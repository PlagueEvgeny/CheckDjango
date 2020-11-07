from django.shortcuts import render

from checkapp.models import Category, Group, Album, Song, Clips


def catalog(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'page_title': 'каталог'
    }

    return render(request, 'checkapp/catalog.html', context)


def index(request):
    return render(request, 'checkapp/index.html')


def group(request, pk):
    Groupes = Group.objects.filter(category_id=pk)
    context = {
        'Groupes': Groupes,
        'page_title': 'страница групп'
    }
    return render(request, 'checkapp/group.html', context)


def album(request, pk):
    albumes = Album.objects.filter(category_id=pk)
    context = {
        'albumes': albumes,
        'page_title': 'страница альбомов'
    }
    return render(request, 'checkapp/album.html', context)


def song(request, pk):
    songes = Song.objects.filter(category_id=pk)
    context = {
        'songes': songes,
        'page_title': 'страница песен'
    }
    return render(request, 'checkapp/song.html', context)


def song_page(request, pk):
    course = Song.objects.get(pk=pk)
    context = {
        'course': course,
        'page_title': 'страница курса'
    }
    return render(request, 'mainapp/course_page.html', context)