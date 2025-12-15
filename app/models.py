from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class Color(models.Model):
    name = models.CharField(max_length=50)
    hex_code = models.CharField(max_length=7, blank=True, null=True)  # #FFFFFF

    def __str__(self):
        return self.name
    
class Size(models.Model):
    name = models.CharField(max_length=20)  # S, M, L, XL, etc.

    def __str__(self):
        return self.name
    

class Product(models.Model):
    image1=models.ImageField(upload_to='products/')
    image2=models.ImageField(upload_to='products/', blank=True, null=True)
    image3=models.ImageField(upload_to='products/', blank=True, null=True)
    image4=models.ImageField(upload_to='products/', blank=True, null=True)
    image5=models.ImageField(upload_to='products/', blank=True, null=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    title = models.CharField(max_length=200)
    description = models.TextField()
    selling_price = models.DecimalField(max_digits=10, decimal_places=0)
    orginal_price = models.DecimalField(max_digits=10, decimal_places=0)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)
    is_new_arrivel = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variants")
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('product', 'color', 'size')

    def __str__(self):
        return f"{self.product.title} - {self.color.name} - {self.size.name}"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('cart', 'product_variant')


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'variant')

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    payment_id = models.CharField(max_length=200, blank=True, null=True) # razorpay/stripe id
    created_at = models.DateTimeField(auto_now_add=True)



