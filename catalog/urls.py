from django.urls import path
from catalog.views import ProductListView, ContactListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView
from catalog.apps import MainConfig
from django.views.decorators.cache import cache_page, never_cache
app_name = MainConfig.name


urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', ContactListView.as_view(), name='contacts'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('create/', never_cache(ProductCreateView.as_view()), name='create_products'),
    path('update/<int:pk>/', never_cache(ProductUpdateView.as_view()), name='product_update'),
    path('delete/<int:pk>/', never_cache(ProductDeleteView.as_view()), name='product_delete')
]