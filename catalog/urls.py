from django.urls import path
from catalog.views import ProductListView, ContactListView, ProductDetailView
from catalog.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', ContactListView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product')
]