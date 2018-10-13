from django.db import models

# Create your models here.

class student(models.Model):
    sname = models.CharField(max_length = 20)
    sage = models.IntegerField()
    sgender = models.BooleanField()
    scontent = models.CharField(max_length = 200)