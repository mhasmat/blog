from django.urls import path
from .api_views import lista_posts_api, lista_usuarios_api, register_api, perfil_usuario_api

urlpatterns = [  
  path('posts/', lista_posts_api, name='lista_posts_api'),  
  path('usuarios/', lista_usuarios_api, name='lista_usuarios_api'),
  
  path('register/', register_api, name='register_api'),
  path('perfil/', perfil_usuario_api, name='perfil_usuario_api'),
]

# GET http://localhost:8000/api/posts/
# GET http://localhost:8000/api/usuarios/
# POST http://localhost:8000/api/register/
# GET http://localhost:8000/api/perfil/