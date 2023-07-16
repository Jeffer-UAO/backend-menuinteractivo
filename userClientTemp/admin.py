from django.contrib import admin

from userClientTemp.models import UserClientTemp


@admin.register(UserClientTemp)
class TableAdmin(admin.ModelAdmin):
    pass
