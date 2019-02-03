from django.db import models
from django.contrib.auth.models import User
from authentication.models import Company
from datetime import datetime


class Resume(models.Model):
    resume = models.FileField(upload_to='forhired-resumes')
    date_posted = models.DateTimeField(auto_now_add=True, blank=True)
