from django.shortcuts import render

def crea_tablero(request):
    return render(request, 'buscamina/crea_tablero.html', {})

# Create your views here.
