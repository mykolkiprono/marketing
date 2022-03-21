from django.contrib import admin
from .models import product

class productAdmin(admin.ModelAdmin):
    pass
admin.site.register(product, productAdmin)
