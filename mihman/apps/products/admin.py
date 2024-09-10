from django.contrib import admin
from .models import Category, Subcategory, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_name', 'slug', 'description')  # Use 'cat_name' instead of 'name'
    prepopulated_fields = {'slug': ('cat_name',)}  # Use 'cat_name' instead of 'name'

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('subcat_name', 'category', 'slug', 'description')  # Use 'subcat_name' instead of 'name'
    prepopulated_fields = {'slug': ('subcat_name',)}  # Use 'subcat_name' instead of 'name'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category', 'subcategory', 'price', 'stock', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
