from django.urls import path

from .views import PhotoAPIView

urlpatterns = [
    path("", PhotoAPIView.as_view(), name="photo_list"),
]
