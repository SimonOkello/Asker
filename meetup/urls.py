from django.urls import path
from meetup import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('home/<int:meetup_id>/', views.detail, name='detail'),
    path('register/', views.register, name='register'),
    path('meetups/', views.meetups, name='meetups'),
    path('meetups/<int:meetup_id>/edit/',
         views.meetup_edit, name='meetup_edit'),
    path('meetups/<int:meetup_id>/delete/',
         views.meetup_delete, name='meetup_delete'),
    path('profile/', views.profile, name='profile'),
    path('password/', views.reset_password, name='reset_password'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')

]
