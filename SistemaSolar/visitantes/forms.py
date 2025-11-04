from django import forms 
from visitantes.models import Visitante  

class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = ['nome_completo', 'data_nascimento', 'email', 'nota', 'comentario']
        widgets = {
            'nota': forms.RadioSelect,  # Define o widget como RadioSelect
        } 