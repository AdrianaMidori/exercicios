from django.shortcuts import render
from visitantes.models import Visitante

def dashboard(request):
    total_visitantes = Visitante.objects.all()

    context = {
        'nome_pagina' : 'Relatório de Visitantes',
        'total_visitantes' : total_visitantes,
    }

    return render(request, "dashboard.html", context)