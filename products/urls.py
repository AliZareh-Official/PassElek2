from django.urls import path
from .views import urunler
urlpatterns = [
    path('urun listesi/', urunler.as_view(), name='urunler'),
]