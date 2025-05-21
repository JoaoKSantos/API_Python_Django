from django.urls import path,include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import FuncionarioViewSet, DepartamentoViewSet

router = DefaultRouter()
router.register(r'funcionarios',FuncionarioViewSet)
router.register(r'departamentos', DepartamentoViewSet)

urlpatterns = [
  
  path('',include(router.urls)),
]