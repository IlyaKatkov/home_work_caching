from django.urls import path
from catalog.views import index
from catalog.views import contacts
from catalog.views import product
from catalog.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/product/', product, name='product')
]