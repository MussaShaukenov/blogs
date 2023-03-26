from django import forms
from .models import Cards, Categories


class CardForm(forms.ModelForm):
    class Meta:
        model = Cards
        fields = ('name', 'description', 'category')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ('name',)


class SearchForm(forms.Form):
    query = forms.CharField()