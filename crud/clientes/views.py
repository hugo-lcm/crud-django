from django.shortcuts import render
from .models import Cliente
from .forms import ClienteForm

# Create your views here.


def listar_clientes(request):
    # faz um select na tabela Cliente e retorna todos os dados
    clientes = Cliente.objects.all()
    # render pra renderizar as infos dos clientes e entre '' o template
    return render(request, 'clientes/listar_clientes.html', {'clientes': clientes})


def inserir_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ClienteForm()
    # a variável form é uma instância do ClienteForm, que cria um formulário com base no models
    return render(request, 'clientes/form_cliente.html', {'form': form})
