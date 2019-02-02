from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)
    user = models.OneToOneField(
        User, null=False, blank=False, on_delete=models.CASCADE)
