from django.db import models

# Create your models here.

class Engwords(models.Model):
    word=models.CharField(max_length=200)
    count=models.IntegerField()
