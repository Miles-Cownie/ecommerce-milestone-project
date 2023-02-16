from django.contrib import admin
from .models import Category, Product_size, Product

# Registration of models to admin panel
admin.site.register(Category)
admin.site.register(Product_size)
admin.site.register(Product)
