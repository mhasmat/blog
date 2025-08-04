from rest_framework import serializers
from .models import Post, Categoria
from django.contrib.auth.models import User

class CategoriaSerializer(serializers.ModelSerializer):
  categoria_post = serializers.SerializerMethodField()

  class Meta:
    model = Categoria
    fields = ['id', 'nombre', 'categoria_post']

  def get_categoria_post(self, obj):
    return {obj.nombre}

class PostSerializer(serializers.ModelSerializer):  
  categoria = CategoriaSerializer()

  class Meta:
    model = Post
    fields = ['id', 'titulo', 'contenido', 'autor', 'fecha_creacion', 'publicado', 'categoria']

class UserSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True)

  class Meta:
    model = User
    fields = ['username', 'email', 'password']

  def create(self, validated_data):
    user = User(
      username = validated_data['username'],
      email = validated_data.get('email', ''),
      is_active = True  # Asegura que el usuario esté activo al registrarse
    )

    # Hash del password
    user.set_password(validated_data['password'])
    user.save()
    
    return user
