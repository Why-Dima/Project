from django.contrib import admin
from motorpool import models


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    pass
