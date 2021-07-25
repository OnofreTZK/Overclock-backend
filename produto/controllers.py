from rest_framework.serializers import ModelSerializer
from .models import Produto

from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework import status

class ProdutoController(ModelSerializer):

    class Meta:
        model = Produto
        fields = ('id', 'nome_produto', 'preco_produto', 'promocao', 'desconto','caminho_imagem')


