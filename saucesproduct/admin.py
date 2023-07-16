from django.contrib import admin
from saucesproduct.models import Sauceproduct


@admin.register(Sauceproduct)
class SauceproductAdmin(admin.ModelAdmin):
    pass
