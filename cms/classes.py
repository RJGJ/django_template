from django.db import models
import datetime


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(null=True, blank=True, default=None)
    updated_at = models.DateTimeField(null=True, blank=True, default=None)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.created_at = datetime.datetime.now()
        super(TimeStampedModel, self).save(*args, **kwargs)

    def update(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now()
        super(TimeStampedModel, self).update(*args, **kwargs)


class SoftDeleteModel(models.Model):
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        self.deleted_at = datetime.datetime.now()
