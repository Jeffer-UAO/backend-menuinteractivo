from django.contrib import admin
from saucesorden.models import Sauceorden


@admin.register(Sauceorden)
class SauceordenAdmin(admin.ModelAdmin):
    pass
