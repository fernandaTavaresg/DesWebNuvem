from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from apiprodutos.views import ProdutoViewSet
from usuarioapi.urls import usuario_router

from django.conf import settings
from django.conf.urls.static import static

router=routers.DefaultRouter()
router.register(r'produtos',ProdutoViewSet)
router.registry.extend(usuario_router.registry)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)