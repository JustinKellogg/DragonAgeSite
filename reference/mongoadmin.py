from mongonaut.sites import MongoAdmin

from .models.item_models import Armor


class ArmorAdmin(MongoAdmin):
    search_field = ('armor_name', 'armor_type')

    list_fields = ('armor_name', 'armor_type', 'cost')

    def has_view_permission(self, request):
        return request.user.is_authenticated and request.user.is_active

Armor.mongoadmin = ArmorAdmin()

