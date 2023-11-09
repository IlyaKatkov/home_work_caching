from django.urls import path
from catalog.views import index
from catalog.views import contacts


urlpatterns = [
    path('', index),
    path('contacts/', contacts)
]