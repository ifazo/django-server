import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from api.users.models import User
from api.products.models import Product


class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review = models.TextField(max_length=255)
    user_id = models.ForeignKey(User, to_field="id", related_name='reviews', on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, to_field="id", related_name='reviews', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Review by {self.user_id} for {self.product_id}'

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'pending'),
        ('processing', 'processing'),
        ('completed', 'completed'),
        ('cancelled', 'cancelled'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    products = models.JSONField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='pending')
    session_id = models.CharField(max_length=255)
    buyer_id = models.ForeignKey(User, to_field="id", related_name='orders', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order {self.id} by {self.buyer_id}'