from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_estoque, name='lista_estoque'),
    path('produto/<int:pk>/', views.detalhes_produto, name='detalhes_produto'),
    path('produto/criar/', views.criar_produto, name='criar_produto'),
    path('produto/editar/<int:pk>/', views.editar_produto, name='editar_produto'),
    path('produto/deletar/<int:pk>/', views.deletar_produto, name='deletar_produto'),
]
