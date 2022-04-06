from xml.etree.ElementInclude import include
from . import views
from django.contrib import admin
from django.urls import path

import travelapp
# virtual enverolment yaseen
urlpatterns = [
    path('', views.demo, name='demo'),
    path('about/', views.about, name='about'),
    path('add/', views.addition, name="addition")
]