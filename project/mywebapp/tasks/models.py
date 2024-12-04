from django.db import models

# Create your models here.
class PlannedTask(models.Model):
    task = models.CharField(max_length=255)