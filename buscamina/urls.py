from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crea_tablero.html', views.crea_tablero, name='crea_tablero'),
    path('drawTable.py', views.drawTable, name='drawTable'),
]