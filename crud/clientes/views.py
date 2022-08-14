from django.shortcuts import render
from .models import Cliente

# Create your views here.


def listar_clientes(request):
    clientes = Cliente.objects.all() # faz um select na tabela Cliente e retorna todos os dados
    return render(request, 'cliente/listar_clientes.html', {'clientes': clientes}) # render pra renderizar as infos dos clientes e entre '' o template
