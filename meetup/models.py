from django.db import models

# Create your models here.
class Meetup(models.Model):
    title = models.CharField(max_length=200)
    venue = models.CharField(max_length=100)
    when = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title