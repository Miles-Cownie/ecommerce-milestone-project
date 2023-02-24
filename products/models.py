from django.db import models


class Category(models.Model):
    # Model for product categories

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product_size(models.Model):

    class Meta:
        verbose_name_plural = 'Product Sizes'

    # Model for storing product sizes
    size = models.CharField(max_length=2)
    size_friendly = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.size

    def get_size_friendly(self):
        return self.size_friendly


class Product(models.Model):

    # Model for storing product details
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    categories = models.ManyToManyField('Category', blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
        )
    size = models.ForeignKey(
        'Product_size', null=True, blank=True, on_delete=models.SET_NULL
        )
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    quantity = models.PositiveIntegerField()
    in_stock = models.BooleanField(default=True)
