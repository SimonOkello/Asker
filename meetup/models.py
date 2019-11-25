from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Members(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username


class Meetup(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='meetings')
    title = models.CharField(max_length=200)
    venue = models.CharField(max_length=100)
    created_on = models.DateTimeField(default=timezone.now)
    when = models.DateField()
    description = models.TextField()
    
    

    def __str__(self):
        return self.title


class Comment(models.Model):
    meetup = models.ForeignKey(
        Meetup, on_delete=models.CASCADE, related_name='comments')
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='comments')
    question = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.question
