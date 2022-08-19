from django.urls import path
from .views import *


urlpatterns = [
    # 1 caminho da url, 2 método que a rota chama, 3 nome da rota (ex no template usa o nome ao inves de http.../clientes/listar)
    path('listar', listar_clientes, name='listar_clientes'),
    path('cadastrar', inserir_cliente, name='cadastrar_cliente')
]
