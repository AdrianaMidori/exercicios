from django.shortcuts import render
from visitantes.forms import VisitanteForm

''' Sugestão de view para processar o formulário de visitante
def visitante_create(request):
    if request.method == 'POST':
        form = VisitanteForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirecionar ou renderizar uma página de sucesso
    else:
        form = VisitanteForm()
    return render(request, 'visitantes/visitante_form.html', {'form': form})
'''

def registrar_visitante(request):
    form = VisitanteForm()
    context = { 
                'nome_pagina': 'Registrar Visitante', 
                'form': form 
               }
    return render(request, 'visitante_form.html', context)
