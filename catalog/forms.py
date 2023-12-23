from django import forms
from catalog.models import Product, Version

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'price',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stop_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        for stopword in self.stop_list:
            if stopword in cleaned_data:
                raise forms.ValidationError('Название содержит недопустимые слова')
        return cleaned_data


    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        for stopword in self.stop_list:
            if stopword in cleaned_data:
                raise forms.ValidationError('Описание содержит недопустимые слова')
        return cleaned_data
class VersionForm(forms.ModelForm):

    class Meta:
         model = Version
         fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'








