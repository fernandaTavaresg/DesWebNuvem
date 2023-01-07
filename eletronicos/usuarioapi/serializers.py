from rest_framework import serializers
from usuarioapi.models import Usuario, Endereco

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usuario
        fields=['id_usuario','nome','cpf','email','data_nascimento','cliente','administrador',
        'senha','foto']

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Endereco
        fields=['id','id_usuario','cep','logradouro','numero','cidade','uf','complemento']

