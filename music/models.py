from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.


class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    year = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)


def __str__(self):
    return self.title
