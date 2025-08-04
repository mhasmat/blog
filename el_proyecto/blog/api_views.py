from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Post
from .serializers import PostSerializer, UserSerializer

@api_view(['GET'])
def lista_posts_api(request):
  posts = Post.objects.filter(publicado=True)
  serializer = PostSerializer(posts, many=True)
  
  return Response(serializer.data)

@api_view(['GET'])
def lista_usuarios_api(request):
  usuarios = User.objects.all()
  serializer = UserSerializer(usuarios, many=True)

  return Response(serializer.data)

@api_view(['POST'])
def register_api(request):
  serializer = UserSerializer(data=request.data)

  if serializer.is_valid():    
    serializer.save()
    
    return Response(serializer.data, status=201)  
  return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def perfil_usuario_api(request):
  """
  Devuelve datos del perfil del usuario autenticado
  """
  user = request.user

  return Response({
    'mensaje': f'Hola, {user.username}',
    'username': user.username,
    'email': user.email,
    'id': user.id
  })
