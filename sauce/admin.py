from django.contrib import admin
from sauce.models import Sauce


@admin.register(Sauce)
class SauceAdmin(admin.ModelAdmin):
    pass
