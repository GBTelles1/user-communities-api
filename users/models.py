import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

# class MyUser(AbstractUser):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Community(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    users = models.ManyToManyField('auth.User', related_name='communities')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
