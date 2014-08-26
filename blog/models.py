from mongoengine import Document, StringField, ReferenceField, ListField, EmbeddedDocument, CASCADE, EmbeddedDocumentField

class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name

class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=120)

    def __unicode__(self):
        return self.name

class Post(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(User, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=30))
    comments = ListField(EmbeddedDocumentField(Comment))

    meta = {'allow_inheritance': True}

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

class TextPost(Post):
    content = StringField()


class ImagePost(Post):
    image_path = StringField()


class LinkPost(Post):
    link_url = StringField()
