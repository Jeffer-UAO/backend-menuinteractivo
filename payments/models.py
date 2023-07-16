from django.db import models

PaymentTypeEnum = (
    ("TARJETA", "Tarjeta"),
    ("EFECTIVO", "Efectivo")
)

StatusPaymentEnum = (
    ("PENDIENTE", "Pendiente"),
    ("PAGADO", "Pagado")
)


class Payment(models.Model):
    table = models.ForeignKey(
        'tables.Table', on_delete=models.SET_NULL, null=True)
    totalPayment = models.DecimalField(max_digits=10, decimal_places=2)
    paymentType = models.CharField(max_length=255, choices=PaymentTypeEnum)
    statusPayment = models.CharField(max_length=255, choices=StatusPaymentEnum)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
