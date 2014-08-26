from rest_framework_mongoengine.serializers import MongoEngineModelSerializer

class BlogSerializer(MongoEngineModelSerializer):
    class Meta:
        model = Blog
        depth = 2
        exclude = ('approved', )
