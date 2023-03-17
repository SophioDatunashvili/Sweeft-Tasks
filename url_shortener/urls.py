from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShortURLViewSet, AccessShortURLView

router = DefaultRouter()
router.register(r'shorten_urls', ShortURLViewSet, basename='shorturl')

urlpatterns = [
    path('', include(router.urls)),
    path('<str:short_name>/', AccessShortURLView.as_view(), name='access_short_url'),
]

