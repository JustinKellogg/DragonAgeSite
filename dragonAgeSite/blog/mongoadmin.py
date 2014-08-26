from mongonaut.sites import MongoAdmin

from .blog.models import Post

Post.mongoadmin = MongoAdmin()
