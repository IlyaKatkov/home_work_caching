from catalog.models import Product, Contact
from django.views.generic import ListView, DetailView


# Create your views here.


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Главная'
    }


class ContactListView(ListView):
    model = Contact
    template_name = 'catalog/contacts.html'



class ProductDetailView(DetailView):
    model = Product














# def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(pk=self.kwargs.get('pk'))
    #     return queryset
    # template_name = 'catalog/product_detail.html'
    #
    # def get_context_data(self, *args, **kwargs):
    #     context_data = super().get_context_data(*args, **kwargs)
    #
    #     product_item = Product.object.get(pk=self.kwargs.get('pk'))
    #     context_data['product_pk'] = product_item.pk
    #     return context_data
