from django.db import models


class Salesman(models.Model):
    description = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.description
