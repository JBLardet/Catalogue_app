from django.contrib import admin

from products.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "description", "price")
    list_editable = ("price",)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
