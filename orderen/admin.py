from django.contrib import admin
from orderen.models import Orderen


@admin.register(Orderen)
class OrderenAdmin(admin.ModelAdmin):
    list_display = ['tipo']
