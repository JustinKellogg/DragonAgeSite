from mongoengine import Document, StringField, IntField
from reference.utility import ARMOR_CHOICES


class Armor(Document):

    armor_name = StringField(max_length=30, required=True)
    description = StringField()
    armor_rating = IntField()
    armor_type = StringField(choices=ARMOR_CHOICES, max_length=5)
    armor_penalty= IntField()
    cost = IntField(help_text="In silver, e.g 30 would be 30 silver")

    slug = StringField(max_length=30, required=True, unique=True)
    meta = {'indexes': ['slug',], 'app_label': 'reference',}

    def __unicode__(self):
        return self.name
