from django import forms

from main.models import Product, Version


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('time_create', 'time_update', 'owner',)

    def _init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

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


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    def _init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
