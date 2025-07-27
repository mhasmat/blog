from rest_framework import serializers
from .models import Post, Categoria

class CategoriaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Categoria
    fields = ['id', 'nombre']

class PostSerializer(serializers.ModelSerializer):
  categoria = CategoriaSerializer(read_only=True)

  class Meta:
    model = Post
    fields = ['id', 'titulo', 'contenido', 'autor', 'fecha_creacion', 'publicado', 'categoria']