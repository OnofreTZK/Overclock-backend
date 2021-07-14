from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):

    id_tipo_usuario = int 
    username = models.TextField()
    email = models.TextField()
    nome = models.TextField()
    telefone = models.TextField()
    cpf = models.TextField()
    data_nascimento = models.DateField()
    # endereco
    # metodos_pagamento
    # carrinho 
    # lista_desejo
    # historico_pedidos
    # lista_chamados


