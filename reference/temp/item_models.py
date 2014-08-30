from mongoengine import *


class Armor(Document):
    name = StringField(required=True)
    description = StringField()
    armor_rating = IntField()
    type = StringField(max_length=30)
    armor_penalty= IntField()
    cost = IntField()

    slug = StringField(max_length=110, required=True, unique=True)
    meta = {'indexes': ['slug',] }

    def __unicode__(self):
        return self.name
