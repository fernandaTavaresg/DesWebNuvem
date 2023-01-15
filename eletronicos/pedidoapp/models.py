from django.db import models
from usuarioapi.models import Usuario

STATUS = [
 (1, 'Cadastrado'),
 (2, 'Faturado'),
 (3, 'Analise'),
 (4, 'Envio'),
 (5, 'Cancelado'),
 (6, 'Concluido'),
]
class Pedido (models.Model):
   id = models.AutoField(primary_key=True)
   id_usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name='Usuario')
   status = models.IntegerField(choices=STATUS, default=1, verbose_name='Status Pedido')
   data = models.DateTimeField(auto_now_add=True, verbose_name='Data do Pedido')
   class Meta:
      ordering=['status']