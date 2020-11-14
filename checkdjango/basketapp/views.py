from django.http import HttpResponseRedirect
from django.shortcuts import render

from basketapp.models import SongBasket
from django.urls import reverse

from checkapp.models import Song


def index(request):
    return render(request, 'basketapp/index.html')


def add(request, songe_id):
    songe = Song.objects.get(pk=songe_id)
    SongBasket.objects.get_or_create(
        user=request.user,
        #songe_id=songe_id
        songe=songe
    )
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    #return HttpResponseRedirect(
    #   reverse('checkapp:song_page',
    #           kwargs={'songe_pk': songe.songe_id})
    #)