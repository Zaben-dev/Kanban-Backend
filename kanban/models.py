from django.db import models


class Tasks(models.Model):
    name = models.CharField(max_length=200)


class Columns(models.Model):
    name = models.CharField(max_length=200)
# Create your models here.
