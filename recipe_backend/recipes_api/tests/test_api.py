from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient, APITestCase
from rest_framework import status

class RecipeListTest(APITestCase):
    fixtures = ['recipes.json', 'ingredients.json', 'recipe_ingredient.json']

    def test_can_make_request_if_not_authenticated(self):
        url = reverse('recipe_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2) # Two fixtures should have been loaded

class RecipeDetailTest(APITestCase):
    fixtures = ['recipes.json', 'ingredients.json', 'recipe_ingredient.json']

    def test_can_make_request_if_not_authenticated(self):
        url = reverse('recipe_detail', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class RecipeUpdateTest(APITestCase):
    fixtures = ['recipes.json', 'ingredients.json', 'recipe_ingredient.json']

    def setUp(self):
        User.objects.create_user(username="test", password="pw")

    def test_unauthenticated_user_cannot_update(self):
        url = reverse('recipe_update', kwargs={'pk': 1})
        data = {
            'name': 'Testing',
            'description': 'test decription',
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_can_update(self):
        url = reverse('recipe_update', kwargs={'pk': 1})
        data = {
            'name': 'Testing'
        }
        self.client.login(username="test", password="pw")
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)