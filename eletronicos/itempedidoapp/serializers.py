from rest_framework import serializers
from itempedidoapp.models import ItemPedido

class ItemPedidoSerializer(serializers.ModelSerializer):
 class Meta:
    model=ItemPedido
    fields=['id','produto','pedido','quantidade']
