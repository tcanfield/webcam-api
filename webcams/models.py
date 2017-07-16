# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Resort(models.Model):
    name = models.CharField(max_length=100)
    resort_url = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Image(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.URLField()
    resort = models.ForeignKey(Resort, related_name='images', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
