from django.urls import path
from .views import register_view, profile_view, tips_view, other_profiles_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
    path('tips/', tips_view, name='tips'),
    path('profiles/', other_profiles_view, name='other_profiles'),
]