from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .api_views import RestaurantViewSet

router = DefaultRouter()
router.register(r'', RestaurantViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

