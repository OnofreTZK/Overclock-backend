from validate_docbr import CPF
from django.contrib.auth.models import User

class UsuarioService(object):

    username = ""
    name = ""
    password = ""
    cpf = ""
    email = ""
    telefone = ""

    def __init__(self, username, name, password, cpf, email, telefone):
        self.username = username
        self.name = name
        self.password = password
        self.cpf = cpf
        self.email = email
        self.telefone = telefone


    def validate_username(self):

        if User.objects.filter(username= self.username).exists():
            return False
        else:
            return True

    def validate_cpf_len(self):

        # Tamanho do padrão nacional para cpf
        if len(self.cpf) == 11:
            return True
        else:
            return False

    def validate_cpf_digits(self):

        digits_validator = CPF()

        '''O CPF é formado por 11 dígitos numéricos que seguem a máscara "###.###.###-##",
        a verificação do CPF acontece utilizando os 9 primeiros dígitos e, com um cálculo simples,
        verificando se o resultado corresponde aos dois últimos dígitos (depois do sinal "-").
        '''
        if digits_validator.validate(self.cpf):
            return True
        else:
            return False

    def validate_email_existence(self):
        if User.objects.filter(email= self.email).exists():
            return False
        else:
            return True

    def validate_email(self):

        if '@' in self.email:
            return True
        else:
            return False

    def validate_email_domain(self):

        if '.com' in self.email:
            return True
        else:
            return False

    def validate_br_phone_number(self):
        if len(self.telefone) == 11:
            return True
        else:
            return False

    def validate_password(self):
        if len(self.password) > 5:
            return True
        else:
            return False

    def validate_name(self):
        treated_string = self.name.lstrip().rstrip()

        if len(treated_string.split(" ")) < 2:
            return False
        else:
            return True





