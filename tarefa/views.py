from django.forms.forms import Form
from django.shortcuts import redirect, render
from .models import TarefaBD
from .forms import ConteudoForm

# Create your views here.
def index(request):
    conteudo = TarefaBD.objects.all()
    form = ConteudoForm()
    
    if request.method == 'POST':
        form = ConteudoForm(request.POST)
        if form.is_valid():
            form=form.save()
            return redirect('/')
    
    context ={
        'conteudos':conteudo,
        
        'form':form
        
    }
    return render(request,'lista.html',context)
