from mongogeneric import ListView, DetailView
from .models import Post, Comment, User

# Create your views here.

class PostListView(ListView):
    model = Post
    queryset = Post.objects.all()


class PostDetailView(DetailView):
    model = Post
    # using this because I show all Post subclasses with same template, otherwise derived from class name
    template_name = "blog/post_detail.html"
    context_object_name = 'post'

    def get_queryset(self):
        return Post.objects.all()    
