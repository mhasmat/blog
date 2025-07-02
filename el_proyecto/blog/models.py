from django.db import models

class Post(models.Model):
  titulo = models.CharField(max_length=200)
  contenido = models.TextField()
  autor = models.CharField(max_length=100)
  fecha_creacion = models.DateTimeField(auto_now_add=True)
  publicado = models.BooleanField(default=False)

  def __str__(self):
    return f"{self.titulo.upper()} - by {self.autor}"
    
class Comentario(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
  autor = models.CharField(max_length=100)
  texto = models.TextField()
  fecha = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"Comentario de {self.autor} | {self.fecha.date()}"