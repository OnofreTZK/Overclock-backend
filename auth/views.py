from django.db import models
from rest_framework.authtoken.views import ObtainAuthToken
from auth.controllers import AuthController

class AuthComToken(ObtainAuthToken):

    controller = AuthController()

    def post(self, request, *args, **kwargs):

        return self.controller.authenticate(self, request)

