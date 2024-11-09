from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Product

class HomeViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('home')
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.product = Product.objects.create(name='Test Product', description='Test Description', price=10.0)

    def test_home_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/home.html')
        self.assertContains(response, 'Bem-vindo ao Patinhas & Caudinhas!')
        self.assertContains(response, self.product.name)

    def test_home_view_post_valid_login(self):
        response = self.client.post(self.url, {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertRedirects(response, reverse('cart'))

    def test_home_view_post_invalid_login(self):
        response = self.client.post(self.url, {
            'username': 'wronguser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/home.html')
        self.assertContains(response, 'Invalid username or password')