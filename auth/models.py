from django.db import models
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from core.models import BearerAuthentication


# Authentication Component
class AuthComToken(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.query_params, context={'request' : request})
        serializer.is_valid(raise_exception=True)

        # User exist's => Retrieve
        user = serializer.validated_data['user']

        # Retrieve or generate a token
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'user-id' : user.pk,
            'token' : token.key,
            'token-type' : BearerAuthentication.keyword,
        })

