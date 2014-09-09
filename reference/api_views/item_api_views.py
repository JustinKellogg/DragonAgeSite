#from reference.models.item_models import *
from reference.models.item_models import *
from reference.serializers.item_serializer import *
from rest_framework_mongoengine.generics import ListAPIView, RetrieveAPIView


class ArmorList(ListAPIView):
    queryset = Armor.objects.all()
    serializer_class = ArmorSerializer

class ArmorDetail(RetrieveAPIView):
    queryset = Armor.objects.all()
    lookup_field = 'slug'
    serializer_class = ArmorSerializer

#weapon
class WeaponList(ListAPIView):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer

class WeaponDetail(RetrieveAPIView):
    queryset = Weapon.objects.all()
    lookup_field = 'slug'
    serializer_class = WeaponSerializer

#shield
class ShieldList(ListAPIView):
    queryset = Shield.objects.all()
    serializer_class = ShieldSerializer

class ShieldDetail(RetrieveAPIView):
    queryset = Shield.objects.all()
    lookup_field = 'slug'
    serializer_class = ShieldSerializer

#gear
class GearList(ListAPIView):
    queryset = Gear.objects.all()
    serializer_class = GearSerializer

class GearDetail(RetrieveAPIView):
    queryset = Gear.objects.all()
    lookup_field = 'slug'
    serializer_class = GearSerializer

class HallucinationList(ListAPIView):
    queryset = Hallucination.objects.all()
    serializer_class = HallucinationSerializer

class HallucinationDetail(RetrieveAPIView):
    queryset = Hallucination.objects.all()
    lookup_field = 'slug'
    serializer_class = HallucinationSerializer

class TrapEffectList(ListAPIView):
    queryset = TrapEffect.objects.all()
    serializer_class = TrapEffectSerializer

class TrapEffectDetail(RetrieveAPIView):
    queryset = TrapEffect.objects.all()
    lookup_field = 'slug'
    serializer_class = TrapEffectSerializer

#trap
class TrapList(ListAPIView):
    queryset = Trap.objects.all()
    serializer_class = TrapSerializer

class TrapDetail(RetrieveAPIView):
    queryset = Trap.objects.all()
    lookup_field = 'slug'
    serializer_class = TrapSerializer

#poison
class PoisonList(ListAPIView):
    queryset = Poison.objects.all()
    serializer_class = PoisonSerializer

class PoisonDetail(RetrieveAPIView):
    queryset = Poison.objects.all()
    lookup_field = 'slug'
    serializer_class = PoisonSerializer

#grenade
class GrenadeList(ListAPIView):
    queryset = Grenade.objects.all()
    serializer_class = GrenadeSerializer

class GrenadeDetail(RetrieveAPIView):
    queryset = Grenade.objects.all()
    lookup_field = 'slug'
    serializer_class = GrenadeSerializer
