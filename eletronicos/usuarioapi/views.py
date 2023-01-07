from django.shortcuts import render
from rest_framework import viewsets
from usuarioapi.models import Usuario, Endereco
from usuarioapi.serializers import UsuarioSerializer, EnderecoSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer


