from django.db import models


class RockCategory(models.Model):
    name = models.CharField(max_length=128)
    desc = models.TextField(blank=True)

class Group(models.Model):
    category = models.ForeignKey(RockCategory,
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    age = models.IntegerField(default=0)

class Album(models.Model):
    category = models.ForeignKey(Group,
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    NumberOfSongs = models.IntegerField(default=0)

class Product(models.Model):
    category = models.ForeignKey(Group,
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    hours = models.IntegerField(default=0)

class Clips(models.Model):
    category = models.ForeignKey(Group,
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    hours = models.IntegerField(default=0)