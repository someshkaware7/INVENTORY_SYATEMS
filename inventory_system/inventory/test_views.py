'''This test case file will test the CRUD operations of the Item model.'''

from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Item, Category

class ItemTests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password123')
        # Login the user
        self.client.login(username='testuser', password='password123')

        # Create a test category
        self.category = Category.objects.create(categoryname="Electronics", description="Electronic items")

    def test_create_item(self):
        data = {
            'itemname': 'Laptop',
            'description': 'A high-performance laptop',
            'quantity': 10,
            'price': 1000.00,
            'sku': 'LAP123',
            'category': self.category.id
        }
        response = self.client.post('/items/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_item(self):
        item = Item.objects.create(
            itemname="Laptop", 
            description="A high-performance laptop", 
            quantity=10, 
            price=1000.00, 
            sku="LAP123", 
            category=self.category
        )
        response = self.client.get(f'/items/{item.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_item(self):
        item = Item.objects.create(
            itemname="Laptop", 
            description="A high-performance laptop", 
            quantity=10, 
            price=1000.00, 
            sku="LAP123", 
            category=self.category
        )
        data = {'quantity': 20}
        response = self.client.put(f'/items/{item.id}/update/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_item(self):
        item = Item.objects.create(
            itemname="Laptop", 
            description="A high-performance laptop", 
            quantity=10, 
            price=1000.00, 
            sku="LAP123", 
            category=self.category
        )
        response = self.client.delete
