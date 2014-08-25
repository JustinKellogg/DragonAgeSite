from django.db import models
from django_mongodb_engine.contrib import MongoDBManager
from djangotoolbox.fields import ListField
from djangotoolbox.fields import EmbeddedModelField


# Create your models here.

class Post(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    tags = ListField()
    comments = ListField(EmbeddedModelField('Comment'))

class Comment(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    author = EmbeddedModelField('Author')
    text = models.TextField()

class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
