from django.db import models
from application.users.models import *
from model_utils.models import TimeStampedModel

# Create your models here.
class Notification(TimeStampedModel):
    notification = models.CharField('Notification',max_length=200)
    dateGenerated = models.DateTimeField('Date Generated')

    def __str__(self):
        return self.name

class UserNotification(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    newNotification = models.ForeignKey(Notification, on_delete=models.CASCADE)

    def __str__(self):
        return self.name