from rest_framework import serializers
from .models import Post, Categoria, Usuario

class CategoriaSerializer(serializers.ModelSerializer):
  categoria_post = serializers.SerializerMethodField()

  class Meta:
    model = Categoria
    fields = ['id', 'nombre', 'categoria_post']

  def get_categoria_post(self, obj):
    return {obj.nombre}

class PostSerializer(serializers.ModelSerializer):
  # categoria = CategoriaSerializer(read_only=True)
  categoria = CategoriaSerializer()

  class Meta:
    model = Post
    fields = ['id', 'titulo', 'contenido', 'autor', 'fecha_creacion', 'publicado', 'categoria']

class UsuarioSerializer(serializers.ModelSerializer):
  class Meta:
    model = Usuario
    fields = '__all__'