from django.urls import path
from . import views, consultas

# ENDPOINTS
app_name = 'blog'
urlpatterns = [
  path('', views.inicio, name='inicio'),
  path('about/', views.about, name='about'),
  path('blog/', views.lista_posts, name='lista_posts'),
  path('post/<int:id>/', views.detalle_post, name='detalle_post'),
  path('categoria/<str:nombre>/', views.posts_categoria, name='posts_categoria'),
  path('consultas/', consultas.consultas, name='consultas'),
  path('buscar/', consultas.buscar_posts, name='buscar'),
]