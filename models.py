from __future__ import unicode_literals
from django.db import models

# Create your models here.


class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    popn = models.PositiveIntegerField()