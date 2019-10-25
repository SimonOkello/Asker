from django.contrib import admin
from meetup.models import Meetup, Comment

# Register your models here.
admin.site.register(Meetup)
admin.site.register(Comment)