from django.db import models

# Create your models here.

class Departamento(models.Model):
  nome=models.CharField(max_length=100)

  def __str__(self):
    return self.nome

class Funcionario(models.Model):
  nome=models.CharField(max_length=100)
  email=models.EmailField(unique=True)
  data_admissao=models.DateField()
  salario= models.FloatField()
  departamento_id=models.ForeignKey(Departamento,on_delete=models.CASCADE,related_name='funcionarios')

  def __str__(self):
    return self.nome