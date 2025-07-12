from django.shortcuts import render, get_object_or_404,  HttpResponseRedirect
from .models import Post, Categoria
from .forms import ComentarioForm

def inicio(request):
  return render(request, 'blog/inicio.html')
    
def about(request):
  return render(request, 'blog/about.html')

def posts_categoria(request, nombre):
  # categorias = Categoria.objects.all()
  # posts = Post.objects.all()
  categoria = get_object_or_404(Categoria, nombre=nombre)
  posts = Post.objects.filter(categoria=categoria)
    
  return render(request, 'blog/posts_categoria.html', {'categoria': categoria, 'posts': posts})

def lista_posts(request):  
  posts = Post.objects.filter(publicado=True).order_by('-fecha_creacion')
  categorias = Categoria.objects.all()

  categoria = Categoria.objects.get(nombre='Programacion')
  posteos = categoria.posts.all()
  print(f"Posteos por Categoría {categoria} \n", posteos)

  return render(request, 'blog/lista_posts.html', {'posts': posts, 'categorias': categorias})

def detalle_post(request, id):
  post = get_object_or_404(Post, id=id, publicado=True)
  comentarios = post.comentarios.all().order_by('-fecha')  
    
  if request.method == 'POST':
    form = ComentarioForm(request.POST)

    if form.is_valid():
      nuevo_comentario = form.save(commit=False)
      nuevo_comentario.post = post
      nuevo_comentario.save()

      return HttpResponseRedirect(request.path) #redirige a la misma página

  else:
    form = ComentarioForm()
    
  return render(request, 'blog/detalle_post.html', {
    'post': post,
    'comentarios': comentarios,
    'form': form
  })