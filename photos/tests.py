from django.test import TestCase
from django.urls import reverse

from .models import Photo


class PhotoTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.photo = Photo.objects.create(
            title="TestCase",
            subtitle="TestSubtitle",
            path="/test/photos/photo.jpg",
            mime_type="image/jpeg",
        )

    def test_photo_content(self) -> None:
        self.assertEqual(self.photo.title, "TestCase")
        self.assertEqual(self.photo.subtitle, "TestSubtitle")
        self.assertEqual(self.photo.path, "/test/photos/photo.jpg")
        self.assertEqual(self.photo.mime_type, "image/jpeg")

    def test_photo_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "TestSubtitle")
        self.assertTemplateUsed(response, "photos/photo_list.html")
