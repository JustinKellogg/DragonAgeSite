from .models import Post
from .serializer import PostSerializer
from rest_framework_mongoengine.generics import ListAPIView, RetrieveAPIView


class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(RetrieveAPIView):
    queryset = Post.objects.all()
    lookup_field = 'slug'
    serializer_class = PostSerializer
