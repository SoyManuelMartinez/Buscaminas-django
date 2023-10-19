from django.urls import path
from . import views

urlpatterns = [
    path('', views.crea_tablero, name='crea_tablero'),
]