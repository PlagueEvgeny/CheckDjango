from django.contrib import admin

from django.contrib import admin

from checkapp.models import Category
from checkapp.models import Group
from checkapp.models import Album
from checkapp.models import Song
from checkapp.models import Clips



admin.site.register(Category)
admin.site.register(Group)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Clips)

