from django import forms

from market.models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'balance', 'price']


class ProductDeleteForm(forms.Form):
    name = forms.CharField(max_length=120, required=True, label='Введите название товара, чтобы удалить его')
