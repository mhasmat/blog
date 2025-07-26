from django.shortcuts import render
from .models import Post, Categoria
from django.db.models.functions import Length
from django.db.models import Q, Count, Avg

def consultas(request):
  posts_all = Post.objects.filter(publicado=True)  
  q_exclude = Post.objects.exclude(autor='admin')
  posts_count = Post.objects.count()
  category_all = Categoria.objects.all().order_by('nombre')
  cat_count = category_all.count()
  first_post = posts_all.filter(autor='admin').first()
  last_post = Post.objects.filter(autor='admin').last()

  contiene = posts_all.filter(titulo__icontains='ia')
  comienza = posts_all.filter(autor__startswith='er').values('titulo', 'autor')
  termina = Post.objects.filter(autor__endswith='h.')
  dia = Post.objects.filter(fecha_creacion__day=2)
  dentro = posts_all.filter(id__in=[4,8,15])
  rango = posts_all.filter(id__range=(1, 5))

  desde_hijo = Post.objects.filter(categoria__nombre='IA')
  desde_padre = Categoria.objects.get(nombre='Clima').posts.all()

  select = Post.objects.select_related('categoria').all()
  print('Select_Related =>', select.query)
  prefetch = Categoria.objects.prefetch_related('posts').all()
  print('Prefetch_Related =>', prefetch.query)

  annotate = Categoria.objects.annotate(total_posts=Count('posts'))
  aggregate = Post.objects.annotate(contenido_len=Length('contenido')).aggregate(promedio_palabras=Avg('contenido_len'))

  return render(request, 'blog/consultas.html', {
    'posts':posts_all,
    'exclude':q_exclude,
    'posts_count':posts_count,
    'categorias':category_all,
    'cat_count':cat_count,
    'first':first_post,
    'last':last_post,
    'contiene':contiene,
    'comienza':comienza,
    'termina':termina,
    'dia':dia,
    'dentro':dentro,
    'rango':rango,
    'desde_hijo':desde_hijo,
    'desde_padre':desde_padre,
    'select':select,
    'prefetch':prefetch,
    'annotate':annotate,
    'aggregate':aggregate,
  })

# def buscar_posts(request):
#   busqueda = request.GET.get('q', '').strip()

#   if busqueda:
#     posts = Post.objects.filter(
#       Q(titulo__icontains=busqueda) | 
#       Q(contenido__icontains=busqueda),
#       publicado=True
#     ).order_by('-fecha_creacion')
#   else:
#     posts = Post.objects.none()

#   return render(request, 'blog/busquedas.html', {
#     'posts':posts,
#     'busqueda':busqueda,
#     'resultados':posts.exists(),
#   })