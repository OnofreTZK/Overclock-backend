from rest_framework.generics import CreateAPIView
from usuario.models import Usuario
from usuario.controllers import UsuarioController

class UsuarioCadastroView(CreateAPIView):

    serializer_class = UsuarioController
    queryset = Usuario.objects.all()
    authentication_classes = []
     
    def create(self, request, *args, **kwargs):
        
        controller = UsuarioController(data=request.data)

        #if controller.is_valid(self):

        return controller.create_user(self)

    @classmethod
    def get_extra_actions(cls):
        return []

