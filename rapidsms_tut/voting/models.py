from django.db import models

class Choice(models.Model):
    name = models.CharField(max_length=40, unique=True)
    votes = models.IntegerField(default=0)
    test= models.CharField(max_length=40)

# Create your models here.
