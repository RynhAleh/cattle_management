from django.contrib import admin
from .models import Cattle


class CattleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Cattle._meta.fields]


admin.site.register(Cattle, CattleAdmin)
