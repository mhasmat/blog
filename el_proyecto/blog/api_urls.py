from django.urls import path
from .api_views import lista_posts_api

urlpatterns = [
  path('posts/', lista_posts_api, name='api_lista_posts'),
]