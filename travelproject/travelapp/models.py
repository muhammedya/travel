from django.db import models
from django.shortcuts import render

# Create your models here.
class Place(models.Model):
    objects = None
    name=models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc=models.TextField()
    def __str__(self):
        return self.name

class MTeam(models.Model):
    objects = None
    tname=models.CharField(max_length=50)
    timg=models.ImageField(upload_to='pics')
    tlang=models.TextField()
    def __str__(self):
        return self.tname


