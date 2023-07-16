from django.db import models


class Sauceproduct(models.Model):
    sauces = models.ForeignKey(
        'sauce.Sauce', on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(
        'products.Product', on_delete=models.SET_NULL, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sauces

