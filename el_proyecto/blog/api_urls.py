from django.urls import path
from .api_views import lista_posts_api, crear_usuario, lista_usuarios

urlpatterns = [  
  path('posts/', lista_posts_api, name='api_lista_posts'),
  path('usuarios/', crear_usuario, name='api_crear_usuario'),
  path('lista-usuarios/', lista_usuarios, name='api_lista_usuarios'),
]

# GET http://localhost:8000/api/posts/
# POST http://localhost:8000/api/usuarios/
# GET http://localhost:8000/api/lista-usuarios/