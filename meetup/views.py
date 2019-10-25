from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, PostMeetup
from django.contrib import auth
from django.contrib.auth import get_user_model
from meetup.models import Meetup
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def home(request):
    meetups = Meetup.objects.all()
    return render(request, 'home.html', {'meetups':meetups})


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
    if request.method == "POST":
        form = PostMeetup(request.POST)
        if form.is_valid():

            form.save()
        return redirect("/meetups")
    else:
        meetups = Meetup.objects.order_by('-when')

    return render(request, 'admin.html', {"meetups": meetups})


def detail(request, meetup_id):
    meetup = get_object_or_404(Meetup, pk=meetup_id)
    return render(request, 'detail.html', {'meetup': meetup})
