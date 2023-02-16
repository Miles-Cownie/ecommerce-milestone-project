from django.contrib import admin
from django.db import models
from django.forms.widgets import CheckboxSelectMultiple
from .models import Category, Product_size, Product


class ProductAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.ManyToManyField: {
            'widget': CheckboxSelectMultiple
        }
    }

    list_display = (
        'sku',
        'name',
        'price',
        'rating',
        'size',
        'image',
        'quantity',
        'in_stock',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ProductSizeAdmin(admin.ModelAdmin):
    list_display = (
        'size_friendly',
        'size',
    )


# Registration of models to admin panel
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product_size, ProductSizeAdmin)
admin.site.register(Product, ProductAdmin)
