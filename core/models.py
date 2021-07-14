from django.db import models
from rest_framework.authentication import TokenAuthentication


# Bearer type token
# -------------------------------------------------------------------------------------------------
class BearerAuthentication(TokenAuthentication):

    keyword = 'Bearer'
# -------------------------------------------------------------------------------------------------


# static class for id user type
# -------------------------------------------------------------------------------------------------
class TipoUsuario(object):
    
    def getId(self, idString):
        return {
            'ADMIN': 0,
            'SUPORTE': 1,
            'JORNALISTA': 2,
            'PESSOA FÍSICA' : 3,
            'PESSOA JURIDICA': 4,
        }[idString]

# -------------------------------------------------------------------------------------------------
