from materials.models import Materials
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from pytils.translit import slugify
from django.urls import reverse
class MaterialCreateView(CreateView):
    model = Materials
    fields = ('title', 'content', 'picture')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('materials:view', args=[self.kwargs.get('pk')])


class MaterialListView(ListView):
    model = Materials

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset

class MaterialDetailView(DetailView):
    model = Materials

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class MaterialUpdateView(UpdateView):
    model = Materials
    fields = ('title', 'content', 'picture')
    success_url = reverse_lazy('materials:list')


class MaterialDeleteView(DeleteView):
    model = Materials
    success_url = reverse_lazy('materials:list')