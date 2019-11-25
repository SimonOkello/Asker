from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, PostMeetup, CommentForm
from django.contrib import auth
from django.contrib.auth import get_user_model, login
from meetup.models import Meetup, Comment
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone


# Create your views here.


def index(request):
    return render(request, 'index.html', {})


@login_required
def home(request):
    meetups = Meetup.objects.all().order_by('-created_on')
    return render(request, 'home.html', {'meetups': meetups})


def register(request):
    """"
    This route is for creating the Asker account by the new user.
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {"form": form})


@login_required
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
                created_by=request.user

            )
            post_meetup.save()

        return redirect("/meetups")
    else:
        meetups = Meetup.objects.all().order_by('-created_on')

    return render(request, 'admin.html', {"meetups": meetups, "form": form})


@login_required
def detail(request, meetup_id):
    # get meeup object
    meetup = get_object_or_404(Meetup, pk=meetup_id)
    # list all active parent questions
    comments = meetup.comments.filter(active=True, parent__isnull=True)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(data=request.POST)
        # question has been added
        if form.is_valid():
            parent_obj = None
            # get parent question_id from the hidden input in the form
            try:
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
                # if parent_id has been submitted get parent_obj id
            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)

                if parent_obj:
                    # create reply object
                    new_reply = form.save(commit=False)
                    # assign parent_obj to reply object
                    new_reply.parent = parent_obj

            new_comment = form.save(commit=False)
            new_comment.meetup = meetup
            new_comment.posted_by = request.user

            new_comment.save()
            return HttpResponseRedirect(reverse('detail', args=(meetup.id,)))
    else:
        form = CommentForm()

    context = {"meetup": meetup, "form": form, "comments": comments}
    return render(request, 'detail.html', context)


def meetup_edit(request, meetup_id):
    meetup = get_object_or_404(Meetup, pk=meetup_id)
    if request.method == "POST":
        form = PostMeetup(request.POST, instance=meetup)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            post.created_on = timezone.now()
            post.save()
            return HttpResponseRedirect(reverse('detail', args=(meetup.id,)))
    else:
        form = PostMeetup(instance=meetup)
    return render(request, 'edit_meetup.html', {'form': form})


def meetup_delete(request, meetup_id):
    """
    This route is for deleting a meeting from the database
    """
    meetup = get_object_or_404(Meetup, pk=meetup_id)
    if request.method == "POST":
        meetup.delete()
        return HttpResponseRedirect(reverse('meetups', args=(meetup.id)))

    return render(request, 'delete.html', {'meetup': meetup})


@login_required
def profile(request):
    meetups = Meetup.objects.all().order_by('-created_on')
    return render(request, 'profile.html', {'meetups': meetups})
