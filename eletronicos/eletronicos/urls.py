from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from apiprodutos.views import ProdutoViewSet

router=routers.DefaultRouter()
router.register(r'produtos',ProdutoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]