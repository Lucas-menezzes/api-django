from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from films.models import Film

class FilmAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.film_data={
            'name': 'Inception',
            'gender': 'Ficção',
            'release_date': '2022-01-01',
            'director': 'Christopher Nolan',
            'actor': 'Leonardo DiCaprio',
            'box_office': '8005000.00',
        }
        self.url=reverse('Movies-list')

def test_create_film(self):
    response = self.client.post(self.url, self.film_data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Film.objects.count(), 1)
    self.assertEqual(Film.objects.get().name, 'Inception')
    
def test_retrieve_film_list(self):
    response = self.client.get(self.url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)