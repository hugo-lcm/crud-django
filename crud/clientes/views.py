from django.shortcuts import render, redirect
from .forms import ClienteForm
from .entidades import cliente
from .services import cliente_service


# Create your views here.


def listar_clientes(request):
    clientes = cliente_service.listar_cliente()
    # render pra renderizar as infos dos clientes e entre '' o template
    return render(request, 'clientes/listar_clientes.html', {'clientes': clientes})


def inserir_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            sexo = form.cleaned_data['sexo']
            data_nascimento = form.cleaned_data['data_nascimento']
            email = form.cleaned_data['email']
            profissao = form.cleaned_data['profissao']
            cliente_novo = cliente.Cliente(nome=nome, sexo=sexo, data_nascimento=data_nascimento,
                                           email=email, profissao=profissao)
            cliente_service.cadastrar_cliente(cliente_novo)
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    # a variável form é uma instância do ClienteForm, que cria um formulário com base no models
    return render(request, 'clientes/form_cliente.html', {'form': form})


def listar_cliente_id(request, id):
    cliente_atual = cliente_service.listar_cliente_id(id)
    return render(request, 'clientes/listar_cliente.html', {'cliente': cliente_atual})


def editar_cliente(request, id):
    cliente_antigo = cliente_service.listar_cliente_id(id)
    form = ClienteForm(request.POST or None, instance=cliente_antigo)
    if form.is_valid():
        nome = form.cleaned_data['nome']
        sexo = form.cleaned_data['sexo']
        data_nascimento = form.cleaned_data['data_nascimento']
        email = form.cleaned_data['email']
        profissao = form.cleaned_data['profissao']
        cliente_novo = cliente.Cliente(nome=nome, sexo=sexo, data_nascimento=data_nascimento,
                                       email=email, profissao=profissao)
        cliente_service.editar_cliente(cliente_antigo, cliente_novo)
        return redirect('listar_clientes')
    return render(request, 'clientes/form_cliente.html', {'form': form})


def remover_cliente(request, id):
    cliente_atual = cliente_service.listar_cliente_id(id)
    if request.method == 'POST':
        cliente_service.remover_cliente(cliente_atual)
        return redirect('listar_clientes')
    return render(request, 'clientes/confirma_exclusao.html', {'cliente': cliente_atual})
