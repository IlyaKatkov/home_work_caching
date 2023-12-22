from catalog.models import Product, Contact, Version
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from catalog.forms import ProductForm


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = str(context['object'])
        context['version'] = Version.objects.filter(product=self.kwargs['pk'], version_indication=True)
        return context

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')
















