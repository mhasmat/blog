from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer, CategoriaSerializer

@api_view(['GET'])
def lista_posts_api(request):
  posts = Post.objects.filter(publicado=True)
  serializer = PostSerializer(posts, many=True)
  
  return Response(serializer.data)

