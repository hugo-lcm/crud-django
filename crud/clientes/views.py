from django.shortcuts import render, redirect
from .forms import ClienteForm
from .models import Cliente


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
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    # a variável form é uma instância do ClienteForm, que cria um formulário com base no models
    return render(request, 'clientes/form_cliente.html', {'form': form})


def listar_cliente_id(request, id):
    cliente = Cliente.objects.get(id=id)  # busca na tabela pelo id passado como parâmetro
    return render(request, 'clientes/listar_cliente.html', {'cliente': cliente})
