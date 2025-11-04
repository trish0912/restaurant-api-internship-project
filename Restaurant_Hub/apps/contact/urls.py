from django.urls import path
from .views import contact_view, about_view

urlpatterns = [
    path('', contact_view, name='contact'),
    path('about/', about_view, name='about'),
]