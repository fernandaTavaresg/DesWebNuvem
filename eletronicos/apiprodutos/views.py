from rest_framework import viewsets
from apiprodutos.models import Produto
from apiprodutos.serializers import ProdutoSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset=Produto.objects.all()
    serializer_class=ProdutoSerializer

'''
Métodos implementados vs métodos http
list -> get(/produtos)
create -> post com payload json(/produtos/)
retrieve -> get com pk (produtos/pk)
update ->  put com pk e payload json (/produtos/pk/)
partial_update -> patch com pk e payload com campos a atualizar(/produtos/pk/)
destroy -> delete com pk(/produtos/pk)
Para implementar mais métodos usar a seguinte combinação disponível em 
https://www.django-rest-framework.org/api-guide/viewsets/#marking-extra-actions-for-routing

'''
