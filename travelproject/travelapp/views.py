from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, MTeam


# Create your views here.
def demo(request):
    obj=Place.objects.all()
    mtobjs = MTeam.objects.all()
    return render(request, "index.html", {'result': obj, 'mtresults': mtobjs})

def about(request):
    return render(request, "about.html")

def addition(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    res=x+y
    return render(request, "result.html", {'resultk':res})
