from django.db import models
from django.utils import timezone

# Create your models here.


class Meetup(models.Model):
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
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)

    def __str__(self):
        return self.text
