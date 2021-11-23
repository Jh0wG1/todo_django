from django import forms
from django.forms import fields
from .models import TarefaBD

class ConteudoForm(forms.ModelForm):
    class Meta:
        model = TarefaBD
        fields= ('conteudo',)
      