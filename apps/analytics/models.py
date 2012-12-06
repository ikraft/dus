from django.db import models
from apps.links.models import Link


class Analytics(models.Model):
    link = models.ForeignKey(Link)
    ip = models.CharField(max_length=16)
    location = models.CharField(max_length=32)
    user_agent = models.CharField(max_length=32)
    referer = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        pass