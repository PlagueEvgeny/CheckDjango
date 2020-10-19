from django.contrib import admin

from django.contrib import admin

from checkapp.models import RockCategory
from checkapp.models import Group
from checkapp.models import Album
from checkapp.models import Product
from checkapp.models import Clips


admin.site.register(RockCategory)
admin.site.register(Group)
admin.site.register(Album)
admin.site.register(Product)
admin.site.register(Clips)
