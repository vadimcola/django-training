from django import forms

from main.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('time_create', 'time_update',)

    def clean_product_name(self):
        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        cleaned_data = self.cleaned_data['product_name']
        cleaned = cleaned_data.upper()
        for word in words:
            if word.upper() in cleaned:
                raise forms.ValidationError("Такое слово нельзя вводить")
            else:
                continue
        return cleaned_data

    def clean_description(self):
        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        cleaned_data = self.cleaned_data['description']
        cleaned = cleaned_data.upper()
        for word in words:
            if word.upper() in cleaned:
                raise forms.ValidationError("Такое слово нельзя вводить")
            else:
                continue
        return cleaned_data
