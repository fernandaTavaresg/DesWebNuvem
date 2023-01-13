from rest_framework import serializers
from apiprodutos.models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Produto
        fields=['id','nome','preco','descricao','quantidade_estoque']