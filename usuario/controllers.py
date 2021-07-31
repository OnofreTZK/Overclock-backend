from rest_framework.serializers import ModelSerializer
from usuario.models import Usuario
from usuario.services import UsuarioService

from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework import status


class UsuarioController(ModelSerializer):

    class Meta:
        model = Usuario
        fields = ('id', 'id_tipo_usuario', 'tipo_usuario', 'username', 'password',
                  'email', 'nome', 'telefone', 'cpf', 'data_nascimento')

    # ID USER TYPE
    def get_user_type(self, id_int):

        return {
            0: 'ADMIN',
            1: 'SUPORTE',
            2: 'JORNALISTA',
            3: 'PESSOA FÍSICA',
            4: 'PESSOA JURIDICA',
        }[id_int]

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
        }[status_code]

    # ERROR RESPONSE
    def error_response(self, status_code, message):

        return Response(status=self.get_error_type(status_code), data= {
            'error' : message,
            'status' : status_code})

    # SERVICE LAYER CALL
    def validate_business_logic(self, request, django_users):

        service = UsuarioService(request['username'],
                                 request['cpf'],
                                 request['email'],
                                 request['telefone'],
                                 django_users)

        if django_users.objects.filter(username=self.request['username']).exists():
            return self.error_response(409,
                                  'Nome de usuário ja existe! Verifique as credenciais.')
        else:

            post_request.perform_create(self)

            headers = post_request.get_success_headers(request.validated_data)

            user = User.objects.create_user(username= request.validated_data['username'],
                                            email= request.validated_data['email'],
                                            password= request.validated_data['password'])

            return self.success_response(201, headers)

    # CREATE USER
    def create_user(self, post_request):

        # Validate serializer(controller) - django requirement
        if self.is_valid(post_request):

            if self.validate_business_logic(self.validated_data, User):
                print("passtest")
            else:
                print("Test")
        else:
            return self.error_response(400,
                                      'Formulário de usuário não foi preenchido corretamente')
