import uuid
from django.db import models
from api.users.models import User
from api.categories.models import Category

# Create your models here.
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    image = models.URLField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    stock = models.IntegerField(default=0)
    category_id = models.ForeignKey(Category, to_field="id", related_name='products', on_delete=models.CASCADE)
    seller_id = models.ForeignKey(User, to_field="id", related_name='products', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name