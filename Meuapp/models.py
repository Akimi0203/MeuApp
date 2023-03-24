from django.db import models
# Create your models here.
#Charfield = tipo de caracteri q vou guardar
#max-length = 100 espaços que eu deixei para aquele dado para ocupar
#null= vai forçar q smp tem um dado lá

class Usuario(models.Model):
      nome = models.CharField(max_length=60, null=True)
      email = models.CharField(max_length=50, null=True)
      cpf = models.CharField(max_length=14, null=True)
      tipo_user = models.CharField(max_length=4, null=True)

      def __str__(self) -> str:
          return self.nome


class Produto(models.Model):
      objects = None
      cod_Produto = models.CharField(max_length=20, null=True)
      descricao = models.CharField(max_length=60, null=True)

      def __str__(self) -> str:
          return self.descricao

class Preco_Produto(models.Model):
      valor = models.FloatField()
      data_valor = models.DateTimeField(auto_now=True)
      cod_produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)

      def __str__(self) -> str:
          return self.cod_produto






