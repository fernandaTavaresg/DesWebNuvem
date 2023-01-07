from rest_framework import routers

from usuarioapi.views import(
    UsuarioViewSet, EnderecoViewSet
)

usuario_router = routers.DefaultRouter()
usuario_router.register('usuario', UsuarioViewSet, basename='usuario-api')
usuario_router.register('endereco', EnderecoViewSet, basename='endereco-api')
