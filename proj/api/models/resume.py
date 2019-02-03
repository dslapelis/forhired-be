from django.db import models
from django.contrib.auth.models import User
from authentication.models import Company
from datetime import datetime


def upload_resume_to(instance, filename):
    import os
    from django.utils.timezone import now
    _, filename_ext = os.path.splitext(filename)
    return 'resumes/%s%s' % (
        now().strftime("%Y%m%d%H%M%S"),
        filename_ext.lower(),
    )


class Resume(models.Model):
    resume = models.FileField(upload_to=upload_resume_to, null=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False)
    date_posted = models.DateTimeField(auto_now_add=True, blank=True)
