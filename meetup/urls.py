from django.urls import path
from meetup import views
urlpatterns = [
    path('', views.index, name = 'index'),
]