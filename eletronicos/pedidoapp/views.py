from django.shortcuts import render
from rest_framework import viewsets
from pedidoapp.models import Pedido
from pedidoapp.serializers import PedidoSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset=Pedido.objects.all()
    serializer_class= PedidoSerializer
