from django.shortcuts import render


def index(request):
    return render(request, 'checkapp/index.html')

