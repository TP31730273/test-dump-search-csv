from django.db import models


# Create your models here.
class CallData(models.Model):
    csv_data = models.JSONField()
