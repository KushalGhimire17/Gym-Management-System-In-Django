from django.urls import path, include
from .views import scanner_view

urlpatterns = [
    path('', scanner_view, name='scanner_view'),
]
