from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from meetup.models import Meetup, Comment, Members


class RegisterForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    phone_number = forms.CharField()
    username = forms.CharField()
    

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "phone_number",
                  "username", "password1", "password2", ]


class PostMeetup(forms.ModelForm):
    title = forms.CharField()
    venue = forms.CharField()
    when = forms.DateInput()
    description = forms.Textarea()

    class Meta:
        model = Meetup
        fields = ['title', 'venue', 'when', 'description']


class CommentForm(forms.ModelForm):
    question = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Comment
        fields = ['question']
