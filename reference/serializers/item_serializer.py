from rest_framework_mongoengine.serializers import MongoEngineModelSerializer
from reference.models.item_models import *


class ArmorSerializer(MongoEngineModelSerializer):
    class Meta:
        model = Armor


class WeaponSerializer(MongoEngineModelSerializer):
    class Meta:
        model = Weapon


class ShieldSerializer(MongoEngineModelSerializer):
    class Meta:
        model = Shield


class GearSerializer(MongoEngineModelSerializer):
    class Meta:
        model = Gear


class HallucinationSerializer(MongoEngineModelSerializer):
    class Meta:
        model = Hallucination


class TrapEffectSerializer(MongoEngineModelSerializer):
    class Meta:
        model = TrapEffect


class TrapSerializer(MongoEngineModelSerializer):
    class Meta:
        model = Trap


class PoisonSerializer(MongoEngineModelSerializer):
    class Meta:
        model = Poison


class GrenadeSerializer(MongoEngineModelSerializer):
    class Meta:
        model = Grenade
