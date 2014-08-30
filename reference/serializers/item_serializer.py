from rest_framework_mongoengine.serializers import MongoEngineModelSerializer
#from reference.models.item_models import Armor
from reference.models.item_models import Armor


class ArmorSerializer(MongoEngineModelSerializer):
    class Meta:
        model = Armor
