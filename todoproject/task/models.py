from django.db import models

# Create your models here.
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    completed = models.BooleanField(default=False)