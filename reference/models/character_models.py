from mongoengine import Document, DynamicEmbeddedDocument


class Attribute(Document):
    pass


class Focus(Document):
    pass


class Origin(Document):
    pass


class Class(Document):
    pass


class Level(Document):
    pass


class Tier(DynamicEmbeddedDocument):
    pass


class Specialization(Document):
    pass
