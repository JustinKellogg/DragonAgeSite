from mongoengine import Document, StringField, IntField, ReferenceField, EmbeddedDocument, EmbeddedDocumentField, ListField, DynamicEmbeddedDocument
from reference.utility import ARMOR_CHOICES, ACTION_CHOICES, WEAPON_GROUP_CHOICES, TIER_CHOICES, SPELL_SCHOOLS, SPELL_TYPES


class Language(Document):
    pass


class Stunt(Document):
    pass


class Action(Document):
    pass


class Requirement(DynamicEmbeddedDocument):
    pass


class MagicalMishaps(Document):

    title = StringField(max_length=30)
    dragon_die = IntField()
    description = StringField()

    slug = StringField(max_length=30, required=True, unique=True)
    meta = {'indexes': ['slug',], 'app_label': 'reference',}


class Spell(Document):

    title = StringField(max_length=30, required=True)
    magic_school = StringField(choices='')
    spell_type = StringField(choices='')
    mana_cost = IntField(help_text="value is in MP (mana points). 5 = 5MP")
    casting_time = StringField(choices='')
    test = StringField()
    requirement = EmbeddedDocumentField(Requirment)
    target_number = IntField()
    description = StringField()

    slug = StringField(max_length=30, required=True, unique=True)
    meta = {'indexes': ['slug',], 'app_label': 'reference',}


class Power(Document):
    pass


class WeaponGroup(Document):
    pass


class Talent(DynamicDocument):
    pass
