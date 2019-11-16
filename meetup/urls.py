from django.urls import path
from meetup import views
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('home/<int:meetup_id>/', views.detail, name='detail'),
    path('register/', views.register, name='register'),
    path('meetups/', views.meetups, name='meetups'),
    path('profile/', views.profile, name='profile'),

]
