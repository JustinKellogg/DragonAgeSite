from rest_framework_mongoengine.serializers import MongoEngineModelSerializer
from .models import Post

class PostSerializer(MongoEngineModelSerializer):
    class Meta:
        model = Post

