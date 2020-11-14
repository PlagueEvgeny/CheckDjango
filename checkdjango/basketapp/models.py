from django.contrib.auth.models import User
from django.db import models

from checkapp.models import Song


class SongBasket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    songe = models.ForeignKey(Song, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)