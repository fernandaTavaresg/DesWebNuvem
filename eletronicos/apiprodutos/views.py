from rest_framework import viewsets,status
from rest_framework.decorators import action
from rest_framework.response import Response
from apiprodutos.models import Produto
from apiprodutos.serializers import ProdutoSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset=Produto.objects.all()
    serializer_class=ProdutoSerializer
    @action(detail=False,methods=['options'])
    def execHttp():
        return Response(None,status=status.HTTP_200_OK)


