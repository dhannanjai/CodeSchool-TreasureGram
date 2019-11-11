from django.shortcuts import render
from django.http import HttpResponse
from .models import Treasure
from .forms import TreasureForm

def homepage_view(request):
    treasures = Treasure.objects.all()
    form = TreasureForm()
    return render(request,'homepage_view.html', {'treasures':treasures, 'form':form})


def details_view(request, treasure_id):
    treasure = Treasure.objects.get(id = treasure_id)
    return render(request,'details_view.html',{'treasure':treasure})

def post_treasure_view(request):
    form = TreasureForm(request.POST)
    if form.is_valid():
        treasure = Treasure(name=form.cleaned_data['name'],
                            value=form.cleaned_data['value'],
                            material=form.cleaned_data['material'],
                            location=form.cleaned_data['location'])
        treasure.save()
    
    return HttpResponseRedirect('')
