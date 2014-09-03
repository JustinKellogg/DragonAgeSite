from mongoengine import Document, StringField, IntField, ReferenceField
from reference.utility import ARMOR_CHOICES, ACTION_CHOICES, WEAPON_GROUP_CHOICES, TIER_CHOICES
from .character_models import Attribute, Focus


class Armor(Document):

    title = StringField(max_length=30, required=True)
    description = StringField()
    armor_rating = IntField()
    armor_type = StringField(choices=ARMOR_CHOICES, max_length=3)
    armor_penalty= IntField()
    cost = IntField(help_text="In silver, e.g 30 would be 30sp")

    slug = StringField(max_length=30, required=True, unique=True)
    meta = {'indexes': ['slug',], 'app_label': 'reference',}

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.title.replace(' ', '_')
        super(Armor, self).save(*args, **kwargs)


class Weapon(Document):

    title = StringField(max_length=30, required=True)
    description = StringField()
    cost = IntField(help_text="In silver, e.g 30 would be 30sp")

    weapon_group = StringField(choices=WEAPON_GROUP_CHOICES, max_length=3)
    damage = StringField(max_length=10)
    damage_attribute = ReferenceField(Attribute)
    attack_attribute = ReferenceField(Attribute) 
    min_strength = IntField()
   
    slug = StringField(max_length=30, required=True, unique=True)
    meta = {'indexes': ['slug',], 'app_label': 'reference', 'allow_inheritance': True}

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.title.replace(' ', '_')
        super(Weapon, self).save(*args, **kwargs)


class MissileWeapon(Weapon):

    min_range = IntField()
    max_range = IntField()
    reload_speed = StringField(choices=ACTION_CHOICES)


class Shield(Document):

    title = StringField(max_length=30, required=True)
    shield_bonus = IntField()
    cost = IntField(help_text="In silver, e.g 30 would be 30sp")
    description = StringField()

    slug = StringField(max_length=30, required=True, unique=True)
    meta = {'indexes': ['slug',], 'app_label': 'reference',}

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.title.replace(' ', '_')
        super(Shield, self).save(*args, **kwargs)



class Gear(Document):

    title = StringField(max_length=30, required=True)
    description = StringField()

    cost = IntField(help_text="In silver, e.g 30 would be 30sp")

    slug = StringField(max_length=30, required=True, unique=True)
    meta = {'indexes': ['slug',], 'app_label': 'reference',}

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.title.replace(' ', '_')
        super(Gear, self).save(*args, **kwargs)


class Hallucination(Document):

    roll_number = IntField()
    title = StringField(max_length=30, required=True)
    description = StringField()

    slug = StringField(max_length=30, required=True, unique=True)
    meta = {'indexes': ['slug',], 'app_label': 'reference',}

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.title.replace(' ', '_')
        super(Hallucination, self).save(*args, **kwargs)


class AdditionalTrapEffect(Document):

    title = StringField(max_length=30, required=True)
    dice_lost = IntField()
    summary = StringField(max_length=30)
    restriction = StringField(choices=TIER_CHOICES)
    description = StringField()

    slug = StringField(max_length=30, required=True, unique=True)
    meta = {'indexes': ['slug',], 'app_label': 'reference',}

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.title.replace(' ', '_')
        super(AdditionalTrapEffect, self).save(*args, **kwargs)


class Trap(Document):

    target_number = IntField()
    base_damage = StringField()
    description = StringField()
    cost = IntField(help_text="In silver, e.g 30 would be 30sp")

    slug = StringField(max_length=30, required=True, unique=True)
    meta = {'indexes': ['slug',], 'app_label': 'reference',}

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = "Trap_" + str(self.target_number)
        super(Trap, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.slug

    def __str__(self):
        return self.slug
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.title.replace(' ', '_')
        super(Trap, self).save(*args, **kwargs)

class Poison(Document):

    title = StringField(max_length=30, required=True)
    poison_level = StringField(choices=TIER_CHOICES)
    raw_cost = IntField(help_text="In silver, e.g 30 would be 30sp")
    prepared_cost = IntField(help_text="In silver, e.g 30 would be 30sp")

    damage = StringField(max_length=10)
    additional_effect = StringField(max_length=20)
    description = StringField()

    slug = StringField(max_length=30, required=True, unique=True)
    meta = {'indexes': ['slug',], 'app_label': 'reference',}

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.title.replace(' ', '_')
        super(Poison, self).save(*args, **kwargs)


class Grenade(Document):

    title = StringField(max_length=30, required=True)
    cost = IntField(help_text="In silver, e.g 30 would be 30sp")
    damage = StringField(max_length=10)
    additional_effect = StringField(max_length=20)
    description = StringField()

    slug = StringField(max_length=30, required=True, unique=True)
    meta = {'indexes': ['slug',], 'app_label': 'reference',}

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.title.replace(' ', '_')
        super(Grenade, self).save(*args, **kwargs)

