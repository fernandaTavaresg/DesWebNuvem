from django.db import models

def upload_foto(instance, filename):
    return f"{instance.id}--{filename}"

Categorias = [
 (1, 'Computadores'),
 (2, 'Games'),
 (3, 'Impressão'),
 (4, 'Telefonia e Tablets'),
 (5, 'Eletroportáteis'),
 (6, 'Câmeras e Vídeos'),
 (7, 'Acessórios'),
 (8, 'Outros'),
]

class Produto(models.Model):
    id=models.AutoField(primary_key=True)
    nome=models.CharField(max_length=100,blank=False)
    preco=models.FloatField()
    descricao=models.TextField()
    quantidade_estoque=models.DecimalField(decimal_places=0,max_digits=10)
    foto=models.ImageField(upload_to=upload_foto, blank=True, null=True)
    categoria = models.IntegerField(choices=Categorias, default=1, verbose_name='Categoria')

    class Meta:
        ordering=['nome']
  
    def __str__(self):
        return self.nome