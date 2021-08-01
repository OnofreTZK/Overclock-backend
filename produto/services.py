from produto.models import Produto

class ProdutoService(object):

    nome_produto = ""
    preco_produto = float
    promocao = bool
    desconto = float
    caminho_imagem = ""

    def __init__(self, nome_produto, preco_produto, promocao, desconto, caminho_imagem):
        self.nome_produto = nome_produto
        self.preco_produto = preco_produto
        self.promocao = promocao
        self.desconto = desconto
        self.caminho_imagem = caminho_imagem


    def validate_name(self):
        if Produto.objects.filter(nome_produto=self.nome_produto).exists():
            return False
        else:
            return True

    def validate_discount(self):
        if self.promocao:
            if self.desconto >= 1 and self.desconto <= 90:
                return True
            else:
                return False
        else:
            if self.desconto == 0:
                return True
            else:
                return False

    def validate_price(self):
        if self.preco_produto > 0:
            return True
        else:
            return False

