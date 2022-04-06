from . import views
from django.urls import path


# virtual enverolment name yaseen
urlpatterns = [

    path('newregister', views.newregister, name='newregister')

]