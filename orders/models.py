from django.db import models


StatusEnum = (
    ("PENDIENTE", "Pendiente"),
    ("ENTREGADO", "Entregado")
)

TipoEnum = (
    ("DM", "Domicilio"),
    ("MS", "Mesa"),
    ("LL", "Llevar")
)


class Order(models.Model):
    table = models.ForeignKey(
        'tables.Table', on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(
        'products.Product', on_delete=models.SET_NULL, null=True, blank=True)
    payment = models.ForeignKey(
        'payments.Payment', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(
        'users.User', on_delete=models.SET_NULL, null=True, blank=True)
    userTemp = models.ForeignKey(
        'userClientTemp.UserClientTemp', on_delete=models.SET_NULL, null=True, blank=True)
    salesman = models.ForeignKey(
        'salesmans.Salesman', on_delete=models.SET_NULL, null=True, blank=True)
    orderen = models.ForeignKey(
        'orderen.Orderen', on_delete=models.SET_NULL, null=True, blank=True)
    tipo = models.CharField(max_length=100, choices=TipoEnum, null=True, blank=True)
    number = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    subtotal = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    salestax = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    status = models.CharField(max_length=255, choices=StatusEnum)
    comment = models.CharField(max_length=255, null=True, blank=True)
    qty = models.PositiveSmallIntegerField(default=0)
    shipto = models.CharField(max_length=255, null=True, blank=True)

    create_at = models.DateTimeField(auto_now_add=True)
    prepared_at = models.DateTimeField(auto_now=True)
    delivered_at = models.DateTimeField(auto_now=True)
    close = models.BooleanField(default=False)
    sauces = models.ManyToManyField('sauce.Sauce', blank=True)

    def __str__(self):
        return str(self.table)
