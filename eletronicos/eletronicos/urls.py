from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from apiprodutos.views import ProdutoViewSet
from usuarioapi.urls import usuario_router
from pedidoapp.views import PedidoViewSet 
from itempedidoapp.views import ItemPedidoViewSet

from django.conf import settings
from django.conf.urls.static import static

router=routers.DefaultRouter()
router.register(r'produtos',ProdutoViewSet)
router.registry.extend(usuario_router.registry)
router.register(r'pedidos',PedidoViewSet), 
router.register(r'itempedido',ItemPedidoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)