from django.contrib import admin

from .models import Product  

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "provider", "added", "updated")
    prepopulated_fields = {"slug": ("name",)}
