from django.shortcuts import render
from .models import Cliente

# Create your views here.


def listar_clientes(request):
    # faz um select na tabela Cliente e retorna todos os dados
    clientes = Cliente.objects.all()
    # render pra renderizar as infos dos clientes e entre '' o template
    return render(request, 'cliente/listar_clientes.html', {'clientes': clientes})
