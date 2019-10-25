from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from meetup.models import Meetup


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class PostMeetup(forms.ModelForm):
    title=forms.CharField()
    venue=forms.CharField()
    when=forms.DateInput()
    description=forms.Textarea()

    class Meta:
        model=Meetup
        fields = ['title', 'venue', 'when', 'description']