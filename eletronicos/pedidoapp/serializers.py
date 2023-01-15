from rest_framework import serializers
from pedidoapp.models import Pedido

class PedidoSerializer(serializers.ModelSerializer):
 class Meta:
    model=Pedido
    fields = ['id','id_usuario', 'status','data']
