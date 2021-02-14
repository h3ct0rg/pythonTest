from model_utils.models import TimeStampedModel
from django.db import models

# Create your models here.
class Role(TimeStampedModel):
    name = models.CharField('Nombre Role',max_length=50)

    def __str__(self):
        return self.name

class User(TimeStampedModel):
    name = models.CharField('Name',max_length=50)
    userName = models.CharField('User Name',max_length=20)
    password = models.CharField('Password',max_length=20)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
