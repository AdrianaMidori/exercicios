from django.shortcuts import render

def index(request):
    
    context = {
        'nome_pagina' : 'Index',
    }

    return render(request, "index.html", context)
