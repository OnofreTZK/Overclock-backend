from rest_framework.serializers import ModelSerializer
from usuario.models import Usuario


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'id_tipo_usuario', 'username', 'email', 'nome', 
                  'telefone', 'cpf', 'data_nascimento')
