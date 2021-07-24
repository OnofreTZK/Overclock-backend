from django.db import models
from rest_framework.authentication import TokenAuthentication


# Bearer type token
class BearerAuthentication(TokenAuthentication):

    keyword = 'Bearer'


