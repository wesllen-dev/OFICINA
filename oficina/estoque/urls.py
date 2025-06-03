from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('novo/', views.novo_item, name='novo_item'),
    path('entrada/<int:item_id>/', views.entrada_estoque, name='entrada'),
    path('saida/<int:item_id>/', views.saida_estoque, name='saida'),
]
