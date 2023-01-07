from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from apiprodutos.views import ProdutoViewSet
from usuarioapi.urls import usuario_router

router=routers.DefaultRouter()
router.register(r'produtos',ProdutoViewSet)
router.registry.extend(usuario_router.registry)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]