from django.urls import path
from .views import content_view

urlpatterns = [
    path('<str:section>/', content_view, name='content'),
]