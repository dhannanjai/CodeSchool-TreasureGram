from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Treasure
from .forms import TreasureForm, LoginForm
from django.contrib.auth import login ,logout, authenticate

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
        treasure = form.save(commit = False)
        treasure.user = request.user
        treasure.save()
    
    return HttpResponseRedirect('/')

def user_profile_view(request,user_name):
    user = User.objects.get(username = user_name)
    treasures = Treasure.objects.filter(user = user)
    return render(request, 'profile_view.html', {'username': user , 'treasures': treasures})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data.get('username')
            p = form.cleaned_data.get('password')
            user = authenticate(username = u, password = p)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print('The Account has been disabled!')
            else:
                print('Authentication failed')
    else:
        form = LoginForm()
        return render(request, 'login_view.html', {'form': form})

def logout_view(request):
    print("Logging out")
    logout(request)
    return HttpResponseRedirect('/')

def like_treasure_view(request):
    treasure_id=request.GET.get('treasure_id', None)

    likes=0
    if (treasure_id):
        treasure = Treasure.objects.get(id=int(treasure_id))

        if treasure is not None:
            likes = treasure.likes+1
            treasure.likes=likes
            treasure.save()
    return HttpResponse(likes)