from django.db import models

class Produto(models.Model):
    id=models.AutoField(primary_key=True)
    nome=models.CharField(max_length=100,blank=False)
    preco=models.DecimalField(decimal_places=2,max_digits=10)
    descricao=models.TextField()
    quantidade_estoque=models.DecimalField(decimal_places=0,max_digits=10)
    
    class Meta:
        ordering=['nome']