from rest_framework.serializers import ModelSerializer
from usuario.models import Usuario
from usuario.services import UsuarioService
from usuario.exceptions import *

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
            406 : status.HTTP_406_NOT_ACCEPTABLE,
        }[status_code]

    # ERROR RESPONSE
    def error_response(self, status_code, message):

        return Response(status=self.get_error_type(status_code), data= {
            'error' : message,
            'status' : status_code})

    # SERVICE LAYER CALL
    def validate_business_logic(self, request):

        service = UsuarioService(request['username'],
                                 request['nome'],
                                 request['password'],
                                 request['cpf'],
                                 request['email'],
                                 request['telefone'])

        # Checking if exist a user with same username
        if not service.validate_username():
            return (False, InvalidUsername)

        if not service.validate_cpf_len():
            return (False, InvalidCpfLen)

        if not service.validate_cpf_digits():
            return (False, InvalidCpfDigits)

        if not service.validate_email_existence():
            return (False, InvalidEmailExist)

        if not service.validate_email():
            return (False, InvalidEmail)

        if not service.validate_email_domain():
            return (False, InvalidEmailDomain)

        if not service.validate_br_phone_number():
            return (False, InvalidBrPhoneNumber)

        if not service.validate_password():
            return (False, InvalidPasswordShort)

        if not service.validate_name():
            return (False, InvalidLastname)
        # else
        return (True, Exception)


    # CREATE USER
    def create_user(self, post_request):

        # Validate serializer(controller) - django requirement
        if self.is_valid(post_request):

            # Getting the validation and the exception
            validated, excepted = self.validate_business_logic(self.validated_data)

            if validated:

                post_request.perform_create(self)

                headers = post_request.get_success_headers(self.validated_data)

                user = User.objects.create_user(username= self.validated_data['username'],
                                                email= self.validated_data['email'],
                                                password= self.validated_data['password'])

                return self.success_response(201, headers)
            else:
                try:
                    raise excepted
                except InvalidUsername:
                    return self.error_response(409,
                                          'Nome de usuário ja existe! Verifique as credenciais.')
                except InvalidCpfLen:
                    return self.error_response(406,
                                          'CPF Inválido -> tamanho fora do padrão nacional.')
                except InvalidCpfDigits:
                    return self.error_response(406,
                                          'CPF Inválido -> digitos não validados.')
                except InvalidEmailExist:
                    return self.error_response(409,
                                          'Email Inválido -> Email ja cadastrado.')
                except InvalidEmail:
                    return self.error_response(406,
                                          'Email Inválido -> string de email esperada é exemplo@exemplo.com.')
                except InvalidEmailDomain:
                    return self.error_response(406,
                                          'Email Inválido -> verifique o dominio do email.')
                except InvalidBrPhoneNumber:
                    return self.error_response(406,
                                          'Telefone Inválido -> formato deve ser 00 00000 0000')
                except InvalidPasswordShort:
                    return self.error_response(406,
                                          'Senha Inválida -> mínimo de 6 caracteres.')
                except InvalidLastname:
                    return self.error_response(406,
                                          'Nome Inválido -> Insira nome e sobrenome.')


        else:
            return self.error_response(400,
                                      'Formulário de usuário não foi preenchido corretamente')
