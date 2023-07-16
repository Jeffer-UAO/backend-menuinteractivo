from django.contrib import admin
from salesmans.models import Salesman


@admin.register(Salesman)
class SalesmanAdmin(admin.ModelAdmin):
    pass
