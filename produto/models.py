from django.db import models

class Produto(models.Model):

    nome_produto = models.TextField(
        verbose_name= 'nome-produto',
        null= False,
        blank= False,
    )

    preco_produto = models.FloatField(
        verbose_name= 'preco-produto',
        default= 0.0,
        null= False,
        blank= False,
    )

    promocao = models.BooleanField(
        default= False,
        null= False,
        blank= True,
    )

    desconto = models.IntegerField(
        default= 0,
        null= False,
        blank= True,
    )

    caminho_imagem = models.TextField(
        verbose_name= 'caminho-imagem',
        null= True,
        blank= True,
    )


