from django.db import models
from simple_history.models import HistoricalRecords


class Table(models.Model):
    number = models.IntegerField(unique=True)
    name = models.CharField(max_length=100, blank=True, null=True, default="")
    history = HistoricalRecords()

    def __str__(self):
        return str(self.number)
