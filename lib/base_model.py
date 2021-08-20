from django.db import models
import uuid
from string import ascii_letters
from random import choice

def uuid_without_dash():
    return uuid.uuid4().hex


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid_without_dash)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False, editable=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        abstract = True
        ordering = ["-timestamp"]

def random_number_gen(number=10):
    return "".join(choice(ascii_letters) + str(i) for i in range(number))
