import uuid
from django.db import models
from django.contrib.auth.hashers import make_password


class User(models.Model):
    ROLE_CHOICES = [
        ('admin', 'admin'),
        ('seller', 'seller'),
        ('buyer', 'buyer'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=255, unique=True)
    image = models.URLField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=255, choices=ROLE_CHOICES, default='buyer')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
