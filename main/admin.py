from django.contrib import admin

from main.models import *


# Register your models here.

@admin.register(Product)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product_name', 'description', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('product_name', 'description',)


@admin.register(Category)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'category_name')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'content', 'picture', 'is_published', 'views')
    prepopulated_fields = {"slug": ("title",)}
