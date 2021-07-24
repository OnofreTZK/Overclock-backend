from rest_framework.serializers import ModelSerializer
from usuario.models import Usuario

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

    # CREATE USER
    def create_user(self, post_request):
       
        if self.is_valid(post_request):
            # If user already exists return error.
            if User.objects.filter(username=self.validated_data['username']).exists(): 
                return self.error_response(409, 
                                      'Nome de usuário ja existe! Verifique as credenciais.')
            else: 
                
                post_request.perform_create(self)

                headers = post_request.get_success_headers(self.validated_data)
            
                user = User.objects.create_user(username= self.validated_data['username'], 
                                                email= self.validated_data['email'],
                                                password= self.validated_data['password'])

                return self.success_response(201, headers)
        else: 
            return self.error_response(400, 
                                      'Formulário de usuário não foi preenchido corretamente')
