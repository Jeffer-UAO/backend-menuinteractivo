from django.contrib import admin
from typeOrders.models import Types


@admin.register(Types)
class TypesAdmin(admin.ModelAdmin):
    pass
