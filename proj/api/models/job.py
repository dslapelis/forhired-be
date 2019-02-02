from django.db import models
from authentication.models import Company
from datetime import datetime


class Job(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)
    description = models.TextField(max_length=2048, null=False, blank=False)
    company = models.ForeignKey(
        Company, null=False, blank=False, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True, blank=True)
