from basketapp.models import SongBasket
from checkapp.models import Song
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse



def index(request):
    items = SongBasket.objects.filter(user=request.user)
    context = {
        'object_list': items,
    }

    return render(request, 'basketapp/basket.html', context)


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

def remove(request, songe_basket_id):
    item = SongBasket.objects.get(id=songe_basket_id)
    item.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))