from django.shortcuts import render
from rest_framework import viewsets
from itempedidoapp.models import ItemPedido
from itempedidoapp.serializers import ItemPedidoSerializer

class ItemPedidoViewSet(viewsets.ModelViewSet):
    queryset=ItemPedido.objects.all()
    serializer_class=ItemPedidoSerializer
