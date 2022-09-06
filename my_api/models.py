from django.db import models
import uuid


class Log(models.Model):
    id = models.UUIDField('id', primary_key=True, default=uuid.uuid4)
    content = models.TextField(max_length=1024)
    date = models.DateTimeField(auto_now_add=True)
