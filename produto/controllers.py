from rest_framework.serializers import ModelSerializer
from produto.models import Produto
from produto.services import ProdutoService
from produto.exceptions import *

from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework import status

class ProdutoController(ModelSerializer):

    class Meta:
        model = Produto
        fields = ('id', 'nome_produto', 'preco_produto', 'promocao', 'desconto','caminho_imagem')

    # SUCCESS TYPE
    def get_success_type(self, status_code):

        return {
            201 : status.HTTP_201_CREATED,
        }[status_code]

    # SUCCESS RESPONSE
    def success_response(self, status_code, headers):

        return Response(self.validated_data, status=self.get_success_type(status_code), headers=headers)

    # ERROR TYPE
    def get_error_type(self, status_code):

        return {
            400 : status.HTTP_400_BAD_REQUEST,
            409 : status.HTTP_409_CONFLICT,
            406 : status.HTTP_406_NOT_ACCEPTABLE,
        }[status_code]

    # ERROR RESPONSE
    def error_response(self, status_code, message):

        return Response(status=self.get_error_type(status_code), data= {
            'error' : message,
            'status' : status_code})

    # SERVICE LAYER CALL
    def validate_business_logic(self, request):

        service = ProdutoService(request['nome_produto'],
                                 request['preco_produto'],
                                 request['promocao'],
                                 request['desconto'],
                                 request['caminho_imagem'])

        if not service.validate_name():
            return (False, InvalidNameExist)

        if not service.validate_discount():
            return (False, InvalidDiscount)

        if not service.validate_price():
            return (False, InvalidPrice)

        # else
        return (True, Exception)

    def create_product(self, post_request):

        # Validate serializer(controller) - django requirement
        if self.is_valid(post_request):

            validated, excepted = self.validate_business_logic(self.validated_data)

            if validated:

                post_request.perform_create(self)

                headers = post_request.get_success_headers(self.validated_data)

                return self.success_response(201, headers)
            else:
                try:
                    raise excepted
                except InvalidDiscount:
                    return self.error_response(406,
                                          'Desconto Inválido!')
                except InvalidNameExist:
                    return self.error_response(409,
                                          'Produto já existente!')
                except InvalidPrice:
                    return self.error_response(406,
                                          'Preço Inválido -> insira um valor maior que 0')
        else:
            return self.error_response(400,
                                      'Formulário de usuário não foi preenchido corretamente')


