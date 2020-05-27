from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class HappyPage(models.Model):
    name = models.CharField(max_length=30)
    content = models.TextField()
    last_update = models.DateTimeField(default=datetime.now())
    
    
class SadPage(models.Model):
    name = models.CharField(max_length=30)
    content = models.TextField()
    last_update = models.DateTimeField(default=datetime.now())
    
    
class ExpectationPage(models.Model):
    name = models.CharField(max_length=30)
    content = models.TextField()
    last_update = models.DateTimeField(default=datetime.now())
    