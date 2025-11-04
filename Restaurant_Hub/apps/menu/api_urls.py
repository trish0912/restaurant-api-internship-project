from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .api_views import MenuItemViewSet

router = DefaultRouter()
router.register(r'', MenuItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
