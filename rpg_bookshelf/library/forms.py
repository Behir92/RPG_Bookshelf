from django import forms
from library.models import Book


class SearchForm(forms.Form):
    title = forms.CharField(label="Tytuł podręcznika", max_length=128)