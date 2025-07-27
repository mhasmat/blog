from django.shortcuts import render
from .models import Post, Categoria
from django.db.models.functions import Length
from django.db.models import Q, Count, Avg
import time

def otras_consultas(request):  
  print('N+1 queries:')
  sin_select = Post.objects.all()  
  print('Sin Select =>', sin_select.query)
  # for post in query:
  #   print(post.categoria.nombre)

  select = Post.objects.select_related('categoria').all()
  print('Select_Related =>', select.query)
  prefetch = Categoria.objects.prefetch_related('posts').all()
  print('Prefetch_Related =>', prefetch.query)

  annotate = Categoria.objects.annotate(total_posts=Count('posts'))
  aggregate = Post.objects.annotate(contenido_len=Length('contenido')).aggregate(promedio_palabras=Avg('contenido_len'))

  only = Post.objects.only('fecha_creacion')
  values = Post.objects.values('id', 'titulo')
  values_list = Post.objects.values_list('titulo', flat=True)
  
  return render(request, 'blog/otras_consultas.html', {
    'select':select,  
    'prefetch':prefetch,
    'annotate':annotate,
    'aggregate':aggregate,
    'only':only,
    'values':values,
    'values_list':values_list, 
  })

def buscar_posts(request):
  busqueda = request.GET.get('q', '').strip()

  if busqueda:
    posts = Post.objects.filter(
      Q(titulo__icontains=busqueda) | 
      Q(contenido__icontains=busqueda),
      publicado=True
    ).order_by('-fecha_creacion')
  else:
    posts = Post.objects.none()

  return render(request, 'blog/busquedas.html', {
    'posts':posts,
    'busqueda':busqueda,
    'resultados':posts.exists(),
  })

def medir_tiempo(request):  
  inicio = time.perf_counter()

  # consulta indicada
  resultados = Post.objects.only('fecha_creacion')[:100]
  
  # fuerza la evaluación de la consulta
  lista_resultados = list(resultados)
  # calcula tiempo transcurrido
  transcurrido = time.perf_counter() - inicio

  contexto = {
    'resultados': lista_resultados,
    'tiempo_ejecucion': f"{transcurrido:.4f}", 
    'total_resultados': len(lista_resultados)
  }

  return render(request, 'blog/resultados.html', contexto)