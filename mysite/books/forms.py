# forms.py
from django import forms

from .models import CartItem


class SearchForm(forms.Form):
    query = forms.CharField(label='', max_length=100,
                            widget=forms.TextInput(attrs={'placeholder': "Search for books...",
                                                          'class': 'search-bar', 'autocomplete': "off"}))

class AddToCartForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['quantity']
        widgets = {
            'quantity': forms.NumberInput(attrs={'min': 1})
        }
