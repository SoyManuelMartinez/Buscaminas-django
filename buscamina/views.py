from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def index(request):
    return render(request, 'buscamina/index.html', {})

def crea_tablero(request):
    filas =     range(1, int( request.GET.get("filas", 0))+1)  # 0 es el valor predeterminado si no se proporciona "filas"
    columnas =  range(1, int( request.GET.get("columnas", 0))+1)  # 0 es el valor predeterminado si no se proporciona "columnas"
    return render(request, 'buscamina/crea_tablero.html', {"filas": filas, "columnas": columnas})

def drawTable(request):
    return render(request, 'buscamina/draw_table.py')

# Create your views here.
