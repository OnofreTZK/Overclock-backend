from validate_docbr import CPF

class UsuarioService(object):

    self.name = ""
    self.cpf = ""
    self.email = ""
    self.telefone = ""

    init(self, name, cpf, email, telefone):
        self.name = name
        self.cpf = cpf
        self.email = email
        self.telefone = telefone


    def cpf_validator(self):
        # Tamanho do padrão nacional para cpf
        if len(cpf) == 11:
            digits_validator = CPF()

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