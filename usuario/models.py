from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):

    id_tipo_usuario = models.IntegerField(
        verbose_name='id-tipo-usuario',
        null= False,
        blank= False,
    )

    tipo_usuario = models.TextField(
        verbose_name='tipo-usuario',
        null= False,
        blank= True
    )

    username = models.TextField(
        null= False,
        blank= False
    )

    password = models.TextField(
        default= 'user.2021',
        null= False,
        blank= False,
    )

    email = models.TextField(
        null= False,
        blank= False,
    )

    nome = models.TextField(
        null= False,
        blank= False
    )

    telefone = models.TextField(
        null= False,
        blank= False,
    )

    cpf = models.TextField(
        null= False,
        blank= False,
    )

    data_nascimento = models.DateField(
        verbose_name= 'data-nascimento',
        null= True,
        blank= True,
    )

    # endereco
    # metodos_pagamento
    # carrinho 
    # lista_desejo
    # historico_pedidos
    # lista_chamados
    

    def __str__(self):
        return self.username


