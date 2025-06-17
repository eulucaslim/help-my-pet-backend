from django.conf import settings
from django.db import models
from register.models import Client
from register.models import Veterinary


class Evaluation(models.Model):
    client = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    veterinary = models.ForeignKey(Veterinary, on_delete=models.PROTECT)
    rating = models.PositiveSmallIntegerField()
    description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
