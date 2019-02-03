from django.db import models
from authentication.models import Company
from datetime import datetime


class Resume(models.Model):
    resume = models.FileField(upload_to='candidate_resumes')
    date_posted = models.DateTimeField(auto_now_add=True, blank=True)
