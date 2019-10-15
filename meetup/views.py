from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import auth
from django.contrib.auth import get_user_model
from meetup.models import Meetup

# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def home(request):
    return render(request, 'home.html', {})


def register(request):
    return render(request, 'signup.html', {})


def home(request):
    return render(request, 'home.html', {})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            form.save()

        return redirect("/login")
    else:
        form = RegisterForm()

    return render(request, 'signup.html', {"form": form})


def meetups(request):
    meetups = Meetup.objects.all()
    context = {
        "meetups": meetups
    }
    return(request, 'admin.html', context)
