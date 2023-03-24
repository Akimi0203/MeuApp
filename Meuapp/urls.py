from django.urls import path
from . import views

urlpatterns = [
    # path('Meuapp/', views.Meuapp, name="Meuapp"),
    path("", views.Meuapp, name='Meuapp'),
    # path("dados/", views.dados, name='dados'),
    path("cons_ultimo/", views.consultar_ultimo, name='cons_ultimo'),
    path("cons_todos/", views.consultar_todos, name='cons_todos'),
    path("produto/", views.raiz_produto, name='raiz_produto'),
    path("gravar/", views.dados, name='dados'),
    path("apagar/<int:id>", views.apagar, name='apagar'),
    path("editar/<int:id>", views.editar, name='editar'),
]
