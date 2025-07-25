from django.urls import path
from .api_views import lista_posts_api, crear_usuario

urlpatterns = [
  path('posts/', lista_posts_api, name='api_lista_posts'),
  path('blog/', lista_posts_api, name='api_lista_posts'),
  path('usuarios/', crear_usuario, name='crear-usuario'),
]