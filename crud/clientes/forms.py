from traceback import format_stack
from django import forms
from .models import Cliente


# validação dos dados antes de inserir no bd
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'sexo', 'profissao',
                  'data_nascimento']  # campos a serem validados
