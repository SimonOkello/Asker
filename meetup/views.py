from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, PostMeetup, CommentForm
from django.contrib import auth
from django.contrib.auth import get_user_model, login
from meetup.models import Meetup, Comment
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse


# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def home(request):
    meetups = Meetup.objects.all().order_by('title')
    return render(request, 'home.html', {'meetups': meetups})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
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
    comments = Comment.objects.filter(parent=None)
    user = User.objects.first()
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            parent_id = request.POST.get('parent_id')
            comment_qs = None
            if parent_id:
                comment_qs = Comment.objects.get(id=parent_id)

            topic.meetup = meetup
            topic.posted_by = user
            topic.parent = comment_qs
            topic.save()
            return HttpResponseRedirect(reverse('detail', args=(meetup.id,)))
    else:
        form = CommentForm()

    context = {"meetup": meetup, "form": form, 'comments': comments}
    return render(request, 'detail.html', context)


def profile(request):
    meetups = Meetup.objects.all().order_by('-created_on')
    return render(request, 'profile.html', {'meetups': meetups})
