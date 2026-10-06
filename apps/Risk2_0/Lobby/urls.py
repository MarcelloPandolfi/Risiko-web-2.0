from django.urls import path
from . import views

urlpatterns = [
    path('Lobby/', views.members, name='Lobby'),
]