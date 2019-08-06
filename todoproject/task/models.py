from django.db import models

# Create your models here.
class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_desc = models.TextField()
    task_com_status = models.BooleanField(default=False)