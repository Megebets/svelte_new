from django.urls import path
from .views import register_view, profile_view, archive_view, home_view, about_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
    path('archive/', archive_view, name='archive'),
    path('home/', home_view, name='home'),
    path('about/', about_view, name='about'),
]