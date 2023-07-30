from django.db import models
from simple_history.models import HistoricalRecords


class Types(models.Model):   
    code = models.CharField(max_length=2, verbose_name='Tipo')
    name = models.CharField(max_length=9, verbose_name='Nombre')
    active = models.BooleanField(default=True, verbose_name='Activo')
    history = HistoricalRecords()

    def __str__(self):
        return str(self.name)
