from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
#from rest_framework.filters import SearchFilter
#from rest_framework.decorators import action
#from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from usuario.models import Usuario
from .serializers import UsuarioSerializer
from rest_framework import status

class UsuarioViewSet(CreateAPIView):

    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()
    authentication_classes = []
    
    def create(self, request, *args, **kwargs):
        
        serializer = UsuarioSerializer(data=request.data)

        if serializer.is_valid(self):
            self.perform_create(serializer.data)
        
            headers = self.get_success_headers(serializer.data)
        

            user = User.objects.create_user(username= serializer.data.username, email= seriializer.data.email,
                                            password= serializer.data.password)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data= {
                'error' : 'formulário de usuário não foi preenchido corretamente',
                'status' : 400})

    @classmethod
    def get_extra_actions(cls):
        return []




