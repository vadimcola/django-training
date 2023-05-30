from django.contrib import admin

from main.models import Product, Category


# Register your models here.

@admin.register(Product)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product_name', 'description', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('product_name', 'description',)


@admin.register(Category)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'category_name')
