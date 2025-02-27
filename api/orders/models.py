import uuid
from django.db import models
from api.users.models import User


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
    