from django.shortcuts import render

def formulario(request):
    return render(request, 'buscamina/formulario.html', {})

# Create your views here.
