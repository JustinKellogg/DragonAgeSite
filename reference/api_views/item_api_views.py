#from reference.models.item_models import *
from reference.models.item_models import Armor
from reference.serializers.item_serializer import ArmorSerializer
from rest_framework_mongoengine.generics import ListAPIView, RetrieveAPIView


class ArmorList(ListAPIView):
    queryset = Armor.objects.all()
    serializer_class = ArmorSerializer

class ArmorDetail(RetrieveAPIView):
    queryset = Armor.objects.all()
    lookup_field = 'slug'
    serializer_class = ArmorSerializer
