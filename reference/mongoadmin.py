from mongonaut.sites import MongoAdmin

#from .models.item_models import Armor
from .models import Armor

class ArmorAdmin(MongoAdmin):
    search_field = ('name', 'type')

    list_fields = ('name', 'type', 'cost')

    def has_view_permission(self, request):
        return request.user.is_authenticated and request.user.is_active

Armor.mongoadmin = ArmorAdmin()

