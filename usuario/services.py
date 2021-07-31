from validate_docbr import CPF
from django.contrib.auth.models import User

class UsuarioService(object):

    name = ""
    cpf = ""
    email = ""
    telefone = ""
    django_users = ""

    def __init__(self, name, cpf, email, telefone, django_users):
        self.name = name
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.django_users = django_users


    def cpf_validator(self):
        digits_validator = CPF()

        # Tamanho do padrão nacional para cpf
        if len(cpf) == 11:

            '''O CPF é formado por 11 dígitos numéricos que seguem a máscara "###.###.###-##",
            a verificação do CPF acontece utilizando os 9 primeiros dígitos e, com um cálculo simples,
            verificando se o resultado corresponde aos dois últimos dígitos (depois do sinal "-").
            '''
            if digits_validator.validate(cpf):
                return True
            else:
                return False
        else:
            return False
