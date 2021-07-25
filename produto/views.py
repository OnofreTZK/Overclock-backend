from rest_framework.viewsets import ModelViewSet
from .models import Produto
from .controllers import ProdutoController

class ProdutoView(ModelViewSet):

    queryset = Produto.objects.all()
    serializer_class = ProdutoController
