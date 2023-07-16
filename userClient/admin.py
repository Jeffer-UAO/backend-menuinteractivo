from django.contrib import admin

from userClient.models import UserClient


@admin.register(UserClient)
class TableAdmin(admin.ModelAdmin):
    pass
