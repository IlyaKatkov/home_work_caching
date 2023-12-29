from django.urls import path
from catalog.views import ProductListView, ContactListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView
from catalog.apps import MainConfig
app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', ContactListView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('create/', ProductCreateView.as_view(), name='create_products'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete')
]