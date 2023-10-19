from django.shortcuts import render
from .models import Post

def index(request):
    return render(request, 'buscamina/index.html', {})

def crea_tablero(request):
    return render(request, 'buscamina/crea_tablero.html', {})

# Create your views here.
