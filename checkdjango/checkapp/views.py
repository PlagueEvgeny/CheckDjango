from django.shortcuts import render


def catalog(request):
    categories = Category.objects.all()
    context = {
        "categories": categories
    }


    return render(request, 'checkapp/catalog.html', context)

def index(request):
    return render(request, 'mainapp/index.html')




