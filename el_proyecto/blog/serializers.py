from rest_framework import serializers
from .models import Post, Usuario

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = ['id', 'titulo', 'contenido', 'autor', 'fecha_creacion', 'publicado']

class UsuarioSerializer(serializers.ModelSerializer):
  class Meta:
    model = Usuario
    fields = '__all__'