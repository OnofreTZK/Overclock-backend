from django.contrib.auth.models import User

class AuthService(object):

    username = ""
    password = ""

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def validate_username(self):
        if User.objects.filter(username= self.username).exists():
            return True
        else:
            return False

    def validate_password(self):
        if len(self.password) < 6:
            return False
        else:
            return True

    def validate_user_password(self):

        if User.objects.filter(username= self.username).exists():
            current_user = User.objects.get(username= self.username)
            if current_user.check_password(self.password):
                return True;
            else:
                return False;
        else:
            return False;
