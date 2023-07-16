from django.db import models


class Orderen(models.Model):
    tipo = models.CharField(max_length=3, null=True, blank=True)


def __str__(self):
    return str(self.tipo)
