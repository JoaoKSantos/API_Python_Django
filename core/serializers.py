from rest_framework import serializers
from .models import Funcionario,Departamento

class DepartamentoSerializer(serializers.ModelSerializer):
  class Meta:
    model=Departamento
    fields='__all__'

class FuncionarioSerializer(serializers.ModelSerializer):
  class Meta:
    model=Funcionario
    fields='__all__'

