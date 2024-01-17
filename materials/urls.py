from django.urls import path
from materials.views import MaterialCreateView, MaterialUpdateView, MaterialListView, MaterialDetailView, MaterialDeleteView
from materials.apps import MaterialsConfig
from django.views.decorators.cache import never_cache
app_name = MaterialsConfig.name

urlpatterns = [
    path('create/', never_cache(MaterialCreateView.as_view()), name='create_materials'),
    path('', MaterialListView.as_view(), name='list'),
    path('view/<int:pk>/', MaterialDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', never_cache(MaterialUpdateView.as_view()), name='update_materials'),
    path('delete/<int:pk>/', never_cache(MaterialDeleteView.as_view()), name='delete_materials')
]