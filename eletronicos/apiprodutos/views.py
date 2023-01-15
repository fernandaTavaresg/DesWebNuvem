from rest_framework import viewsets
from apiprodutos.models import Produto
from apiprodutos.serializers import ProdutoSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset=Produto.objects.all()
    serializer_class=ProdutoSerializer


