from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, PostMeetup, CommentForm
from django.contrib import auth
from django.contrib.auth import get_user_model
from meetup.models import Meetup, Comment
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def home(request):
    meetups = Meetup.objects.all().order_by('title')
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                text=form.cleaned_data["text"],
                meetups=meetups,
            )
            comment.save()
            form = CommentForm()
    return render(request, 'home.html', {'meetups': meetups, 'form': form})


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
    form = PostMeetup()
    if request.method == "POST":
        form = PostMeetup(request.POST)
        if form.is_valid():
            post_meetup = Meetup(
                title=form.cleaned_data["title"],
                venue=form.cleaned_data["venue"],
                when=form.cleaned_data["when"],
                description=form.cleaned_data["description"],

            )
            post_meetup.save()

        return redirect("/meetups")
    else:
        meetups = Meetup.objects.all().order_by('-created_on')

    return render(request, 'admin.html', {"meetups": meetups, "form": form})


def detail(request, meetup_id):
    meetup = get_object_or_404(Meetup, pk=meetup_id)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                text=form.cleaned_data["text"],
                meetup=meetup,
            )
            comment.save()
            form = CommentForm()

    context = {"meetup": meetup, "form": form}
    return render(request, 'detail.html', context)


def profile(request):
    meetups = Meetup.objects.all().order_by('-created_on')
    return render(request, 'profile.html', {'meetups': meetups})
