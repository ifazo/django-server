import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from api.users.models import User
from api.products.models import Product

# Create your models here.

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
