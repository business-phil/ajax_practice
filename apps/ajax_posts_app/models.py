from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
    """
    Model for post resource; only needs 'description' field
    """
    description = models.TextField()
