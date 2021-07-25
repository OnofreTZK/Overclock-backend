from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers

# Auth
from auth.views import AuthComToken

# Usuario
from usuario.views import UsuarioCadastroView

# Produto
from produto.views import ProdutoView


router = routers.DefaultRouter()
router.register(r'produto', ProdutoView, basename='produtosCRUD')

urlpatterns = [
    path('', include(router.urls)),
    path('usuario/cadastro/', UsuarioCadastroView.as_view()),
    path('admin/', admin.site.urls),
    path('auth/', AuthComToken.as_view()),
]
