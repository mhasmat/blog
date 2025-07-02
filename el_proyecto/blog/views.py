from django.shortcuts import render
from .models import Post

def inicio(request):
  return render(request, 'blog/inicio.html')
    
def about(request):
  return render(request, 'blog/about.html')

def lista_posts(request):
  posts = Post.objects.filter(publicado=True).order_by('-fecha_creacion')
  return render(request, 'blog/lista_posts.html', {'posts': posts})