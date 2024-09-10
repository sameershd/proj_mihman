from django.db import models

class Category(models.Model):
    cat_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)  # For URL-friendly representation
    description = models.TextField(max_length=250, blank=True)
    cat_img = models.ImageField(upload_to="photos/categories", blank=True, null=True)

    def __str__(self):
        return self.cat_name

class Subcategory(models.Model):
    subcat_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=100, unique=True)  # For URL-friendly representation
    description = models.TextField(max_length=200, blank=True)
    subcat_img = models.ImageField(upload_to="photos/subcategories", blank=True, null=True)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)

    def __str__(self):
        return self.subcat_name

class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)  # For URL-friendly representation
    description = models.TextField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    subcategory = models.ForeignKey(Subcategory, related_name='products', on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, blank=True, null=True)  # New field

    def __str__(self):
        return self.product_name

