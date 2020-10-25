from django.db import models
import datetime


class Category(models.Model):
    name = models.CharField(max_length=128)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Group(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Album(models.Model):
    category = models.ForeignKey(Group,
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    number_of_songs = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

class Song(models.Model):
    category = models.ForeignKey(Album,
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    time = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'

class Clips(models.Model):
    category = models.ForeignKey(Song,
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    time = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клип'
        verbose_name_plural = 'Клипы'