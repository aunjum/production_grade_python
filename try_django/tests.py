# myapp/tests.py

from django.test import TestCase, Client
from django.urls import reverse

class MyViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_my_view(self):
        url = reverse('my-view')
        response = self.client.post(url, {'data': 5})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('result'), 10)

    def test_my_view_with_no_data(self):
        url = reverse('my-view')
        response = self.client.post(url, {})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json().get('error'), 'An error occurred. Please try again.')
