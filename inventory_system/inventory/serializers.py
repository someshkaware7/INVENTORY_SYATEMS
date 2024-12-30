from rest_framework import serializers
from .models import Item, Category

# Serializer for Category model
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'categoryname', 'description', 'created_at', 'updated_at']

# Serializer for Item model
class ItemSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())  # Nested serializer for category details

    class Meta:
        model = Item
        fields = ['id', 'itemname', 'description', 'quantity', 'price', 'sku', 'category', 'status', 'supplier', 'created_at', 'updated_at']
