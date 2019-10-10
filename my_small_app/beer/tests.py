from django.urls import reverse
from rest_framework.test import RequestsClient, APITestCase
from rest_framework import status
from .models import BeerModel, WhiskeyModel


class APITests(APITestCase):

    def test_whiskey_views(self):
        data = {
            'brand': 'Black Ram',
            'age': 12,
            'description': 'Bulgarian brand of whiskey, do not buy.'
        }
        post_response = self.client.post(reverse('beer:whiskey-post-get-views'), data, format='json')

        self.assertEqual(post_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(WhiskeyModel.objects.count(), 1)
        self.assertEqual(WhiskeyModel.objects.get().brand, 'Black Ram')

        response = self.client.get(reverse('beer:whiskey-post-get-views'))
        self.assertEquals(response.status_code, 200)

    def test_beer_views(self):
        data = {
            'name': 'Kamenitza',
            'description': 'very good and tasty beer'
        }
        post_response = self.client.post(reverse('beer:beer-post'), data, format='json')

        self.assertEqual(post_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BeerModel.objects.count(), 1)
        self.assertEqual(BeerModel.objects.get().name, 'Kamenitza')

        get_response = self.client.get(reverse('beer:beer-get', kwargs={'pk': 1}))
        self.assertEquals(get_response.status_code, 200)
