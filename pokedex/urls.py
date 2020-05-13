from django.urls import path
from . import views

urlpatterns = [
    path('', views.pokedex, name='Pokedex'),
    path('<str:pokemon>/', views.pokemon, name='Pokemon')
]