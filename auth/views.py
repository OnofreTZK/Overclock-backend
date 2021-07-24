from django.db import models
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from auth.models import BearerAuthentication
from auth.controllers import AuthController

class AuthComToken(ObtainAuthToken):

    controller = AuthController()
    
    def post(self, request, *args, **kwargs):

        token, user = self.controller.authenticate(self, request)

        return Response({
            'user-id' : user.pk,
            'token' : token.key,
            'token-type' : BearerAuthentication.keyword,
        })
