from django.contrib import admin
from .models import Category, Product

# Registration of models to admin panel
admin.site.register(Product)
admin.site.register(Category)
