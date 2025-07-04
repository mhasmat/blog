from django.shortcuts import render, get_object_or_404,  HttpResponseRedirect
from .models import Post
from .forms import ComentarioForm

def inicio(request):
  return render(request, 'blog/inicio.html')
    
def about(request):
  return render(request, 'blog/about.html')

def lista_posts(request):
  posts = Post.objects.filter(publicado=True).order_by('-fecha_creacion')
  return render(request, 'blog/lista_posts.html', {'posts': posts})

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