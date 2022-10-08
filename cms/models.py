from django.db import models
from .classes import SoftDeleteModel, TimeStampedModel
from django.utils.text import slugify
import uuid


class MetaData(TimeStampedModel, SoftDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.TextField(max_length=255)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.title


class Page(TimeStampedModel, SoftDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.TextField(max_length=255)
    slug = models.TextField(max_length=255, blank=True, default='', null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug(slugify(self.title))
        super(Page, self).save(*args, **kwargs)


class ArticleCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.TextField(max_length=255)
    parent = models.ForeignKey('self', blank=True, null=True, default=None, on_delete=models.CASCADE)


class Article(models.Model):
    pass 
