from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from photos.models import Photo


class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.photo = Photo.objects.create(
            title='Test Photo',
            subtitle='Test Subtitle',
            path='/test/photos/test_photo.jpg',
            mime_type='image/jpeg',
        )

    def test_api_listview(self):
        response = self.client.get(reverse('photo_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Photo.objects.count(), 1)
        self.assertContains(response, self.photo)
