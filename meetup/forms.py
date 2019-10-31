from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from meetup.models import Meetup, Comment


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class PostMeetup(forms.ModelForm):
    title = forms.CharField()
    venue = forms.CharField()
    when = forms.DateInput()
    description = forms.Textarea()

    class Meta:
        model = Meetup
        fields = ['title', 'venue', 'when', 'description']


class CommentForm(forms.ModelForm):
    author = forms.CharField()
    text = forms.Textarea()

    class Meta:
        model = Comment
        fields = ['author', 'text']


class PostQuizForm(forms.ModelForm):
    meetup = forms.ModelChoiceField(
        queryset=Meetup.objects.all().order_by('-created_on'))
    author = forms.CharField()
    text = forms.Textarea()

    class Meta:
        model = Comment
        fields = ['author', 'meetup', 'text']
    
