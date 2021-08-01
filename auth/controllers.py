from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status

from auth.models import BearerAuthentication
from auth.services import AuthService
from auth.exceptions import *

class AuthController(object):

     # SERVICE LAYER CALL
    def validate_business_logic(self, request):

        service = AuthService(request['username'], request['password'])

        if not service.validate_username():
            return (False, InvalidUsername)

        if not service.validate_password():
            return (False, InvalidPassword)

        if not service.validate_user_password():
            return (False, InvalidWrongPassword)

        # else
        return (True, Exception)


    def authenticate(self, auth_request, request):

        serializer = auth_request.serializer_class(data=request.data, context={'request' : request})

        if serializer.is_valid():

            validated, excepted = self.validate_business_logic(serializer.validated_data)

            if validated:

                # User exist's => Retrieve
                user = serializer.validated_data['user']

                # Retrieve or generate a token
                token, created = Token.objects.get_or_create(user=user)

                return Response(status= status.HTTP_200_OK, data= {
                    'user-id' : user.pk,
                    'token' : token.key,
                    'token-type' : BearerAuthentication.keyword,
                })

            else:
                try:
                    raise excepted
                except InvalidUsername:
                    return Response(status= status.HTTP_406_NOT_ACCEPTABLE, data= {
                        'error' : 'Usuário não existente.',
                        'status' : 406,
                    })
                except InvalidPassword:
                    return Response(status= status.HTTP_400_BAD_REQUEST, data= {
                        'error' : 'Senha inválida.',
                        'status' : 400,
                    })
                except InvalidWrongPassword:
                    return Response(status= status.HTTP_401_UNAUTHORIZED, data= {
                        'error' : 'Senha incorreta.',
                        'status' : 401,
                    })
        else:
            return Response(status= status.HTTP_400_BAD_REQUEST, data= {
                'error' : 'Nome de usuário e/ou senha incorreto(s).',
                'status' : 400,
            })
