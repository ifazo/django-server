from rest_framework import serializers
from api.reviews.serializers import ReviewSerializer
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
