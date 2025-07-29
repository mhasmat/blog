from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post, Usuario
from .serializers import PostSerializer, UsuarioSerializer

@api_view(['GET'])
def lista_posts_api(request):
  posts = Post.objects.filter(publicado=True)
  serializer = PostSerializer(posts, many=True)
  
  return Response(serializer.data)

@api_view(['POST'])
def crear_usuario(request):
  serializer = UsuarioSerializer(data=request.data)

  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=201)
  return Response(serializer.errors, status=400)

@api_view(['GET'])
def lista_usuarios(request):
  usuarios = Usuario.objects.all()
  serializer = UsuarioSerializer(usuarios, many=True)

  return Response(serializer.data)
