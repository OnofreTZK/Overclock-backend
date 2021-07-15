from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from auth.models import AuthComToken
from usuario.api.viewsets import UsuarioViewSet
from rest_framework import routers
from usuario.api.viewsets import UsuarioViewSet


router = routers.DefaultRouter()
router.register(r'usuario', UsuarioViewSet, basename='UsuarioViewSet')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', AuthComToken.as_view()),
]
