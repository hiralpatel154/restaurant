from django.db import models

# Create your models here.

class Hotel(models.Model):
    resname = models.CharField(max_length=40, null=True)
    reslink = models.CharField(max_length=40, null=True)

class Indian(models.Model):
    image = models.FileField(null=True)
    desc = models.TextField(max_length=540, null=True)