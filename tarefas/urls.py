from django.urls import path

from . import views

urlpatterns = [
    path('', views.lista_tarefas, name='lista_tarefas'),
    path('remover/<int:tarefa_id>/', views.remover, name='remover'),
]