from django.shortcuts import render
from django.http import HttpResponse
from .models import Treasure

def homepage_view(request):
    treasures = Treasure.objects.all()
    return render(request,'homepage_view.html', {'treasures':treasures})
