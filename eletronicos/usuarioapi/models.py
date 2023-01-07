from django.db import models

class Usuario(models.Model):
    id=models.AutoField(primary_key=True)
    nome=models.CharField(max_length=100,blank=False, verbose_name='Nome')
    cpf=models.CharField(max_length=11, verbose_name='CPF')
    email=models.CharField(max_length=100, verbose_name='E-mail')
    data_nascimento=models.DateField(null=True, blank=True)
    cliente=models.BooleanField(verbose_name='Cliente')
    administrador=models.BooleanField(verbose_name='Fornecedor')
    senha=models.CharField(max_length=50)

    class Meta:
        ordering = ['nome']

class Endereco(models.Model):
    id=models.AutoField(primary_key=True)
    id_usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name='Usuario')
    cep=models.CharField(max_length=8, verbose_name='CEP')
    logradouro=models.CharField(max_length=100, verbose_name='Logradouro')
    numero= models.CharField(max_length=10, verbose_name='Numero')
    cidade=models.CharField(max_length=100, verbose_name='Cidade')
    uf=models.CharField(max_length=2, verbose_name='Estado')
    complemento=models.TextField(null=True, blank=True, verbose_name='Complemento')

    class Meta:
        ordering = ['logradouro']

