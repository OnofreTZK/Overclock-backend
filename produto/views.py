from rest_framework.viewsets import ModelViewSet
from .models import Produto
from .controllers import ProdutoController

class ProdutoView(ModelViewSet):

    queryset = Produto.objects.all()
    serializer_class = ProdutoController

    def create(self, request, *args, **kwargs):

        controller = ProdutoController(data=request.data)

        return controller.create_product(self)
