from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from usuario.models import Usuario
from .serializers import UsuarioSerializer


class UsuarioViewSet(ModelViewSet):

    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()



    '''
    #POST
    def create(self, request, *args, **kwargs):

        # Validate credentials
        user_credentials = request.query_params

        users = get_user_model().objects.all()

        if users.count(get_username() == user_credentials['username']) > 0:
            #response.status_code = 400
            #response['error'] = "Usuário ja existe, por favor verifique as credenciais!"
            #return response

        user = User.objects.create_user(user_credentials['username'], user_credentials['email'],
                                            user_credentials['password'])
                                            

        # Validate data
        user_form_data = request.data
    '''


