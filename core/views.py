from django.shortcuts import render
from rest_framework import viewsets
from .models import Funcionario,Departamento
from .serializers import FuncionarioSerializer, DepartamentoSerializer
# Create your views here.

class FuncionarioViewSet(viewsets.ModelViewSet):
  queryset=Funcionario.objects.all()
  serializer_class= FuncionarioSerializer

class DepartamentoViewSet(viewsets.ModelViewSet):
  queryset=Departamento.objects.all()
  serializer_class= DepartamentoSerializer
