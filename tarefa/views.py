from django.shortcuts import render
from .models import TarefaBD

# Create your views here.
def index(request):
    conteudo = TarefaBD.objects.all()
    context ={
        'conteudos':conteudo
    }
    return render(request,'lista.html',context)
