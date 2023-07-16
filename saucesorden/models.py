from django.db import models


class Sauceorden(models.Model):
    sauces = models.ForeignKey(
        'sauce.Sauce', on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(
        'orders.Order', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.sauces
