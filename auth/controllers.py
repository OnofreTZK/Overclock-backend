from rest_framework.authtoken.models import Token

class AuthController(object):

    def authenticate(self, auth_request, request):
 
        serializer = auth_request.serializer_class(data=request.data, context={'request' : request})
        serializer.is_valid(raise_exception=True)

        # User exist's => Retrieve
        user = serializer.validated_data['user']

        # Retrieve or generate a token
        token, created = Token.objects.get_or_create(user=user)

        return token, user
