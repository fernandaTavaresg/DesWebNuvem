from django.db import models
from apiprodutos.models import Produto
from pedidoapp.models import Pedido

class ItemPedido(models.Model):
 id=models.AutoField(primary_key=True)
 produto = models.ForeignKey(Produto, on_delete=models.CASCADE, verbose_name='Produto')
 pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, verbose_name='Pedido')
 quantidade = models.DecimalField(decimal_places=2,max_digits=10, verbose_name='Quantidade')
 class Meta:
    db_table = 'ItemPedido'