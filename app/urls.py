
from django.urls import path, include
from .views.tarefa_views import *
from .views.usuario_views import *
urlpatterns = [
    path('lista_tarefas/', listar_tarefas, name='listar_tarefas'),
    path('cadastra_tarefas/', cadastrar_tarefa, name='cadastra_tarefa'),
    path('editar_tarefas/<int:id>', editar_tarefas, name='editar_tarefa'),
    path('remover_tarefas/<int:id>', remover_tarefa, name='remover_tarefa'),
    path('cadastrar_usuario/', cadastrar_usuario, name='cadastrar_usuario'),
    path('logar_usuario/', logar_usuario, name='logar_usuario'),
    path('deslogar_usuario/', deslogar_usuario, name='deslogar_usuario'),
]

