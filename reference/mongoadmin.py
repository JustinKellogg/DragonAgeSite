from mongonaut.sites import MongoAdmin

from .models.item_models import *


class ArmorAdmin(MongoAdmin):
    search_field = ('title', 'armor_type')
    list_fields = ('title', 'armor_type', 'cost')

    def has_view_permission(self, request):
        return request.user.is_authenticated and request.user.is_active

Armor.mongoadmin = ArmorAdmin()

class WeaponAdmin(MongoAdmin):
    search_fields = ('title', 'weapon_group')
    list_fields = ('title', 'weapon_group', 'cost')

    def has_view_permission(self, request):
        return request.user.is_authenticated and request.user.is_active

Weapon.mongoadmin = WeaponAdmin()


class ShieldAdmin(MongoAdmin):
    search_fields = ('title')
    list_fields = ('title', 'shield_bonus', 'cost')
    
    def has_view_permission(self, request):
        return request.user.is_authenticated and request.user.is_active

Shield.mongoadmin = ShieldAdmin()


class GearAdmin(MongoAdmin):
    search_fields = ('title')
    list_fields = ('title', 'cost')

    def has_view_permission(self,request):
        return request.user.is_authenticated and request.user.is_active

Gear.mongoadmin = GearAdmin()

class HallucinationAdmin(MongoAdmin):
    search_fields = ('title')
    list_fields = ('title', 'roll_number')

    def has_view_permission(self,request):
        return request.user.is_authenticated and request.user.is_active

Hallucination.mongoadmin = HallucinationAdmin()

class TrapEffectAdmin(MongoAdmin):
    search_fields = ('title')
    list_fields = ('title', 'summary', 'restriction')

    def has_view_permission(self,request):
        return request.user.is_authenticated and request.user.is_active

TrapEffect.mongoadmin = TrapEffectAdmin()

class PoisonAdmin(MongoAdmin):
    search_fields = ('title', 'poison_level', 'additional_effect')
    list_fields = ('title', 'poison_level', 'additional_effect')

    def has_view_permission(self,request):
        return request.user.is_authenticated and request.user.is_active

Poison.mongoadmin = PoisonAdmin()

class TrapAdmin(MongoAdmin):
    search_fields = ()
    list_fields = ('target_number', 'base_damage')

    def has_view_permission(self,request):
        return request.user.is_authenticated and request.user.is_active

Trap.mongoadmin= TrapAdmin()

class GrenadeAdmin(MongoAdmin):
    search_fields = ('title', 'additional_effect')
    list_fields = ('title', 'additional_effect', 'cost')

    def has_view_permission(self,request):
        return request.user.is_authenticated and request.user.is_active

Grenade.mongoAdmin = GrenadeAdmin()
