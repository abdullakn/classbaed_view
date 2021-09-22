from django import forms
from django.db import models
from django.forms.widgets import Widget
from . models import Book



class AddForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=('title','genre','author','isbn')

    Widgets={
        'title':forms.TextInput(attrs={'class':'form-control'}),
        'genre':forms.TextInput(attrs={'class':'form-control'}),
        'author':forms.TextInput(attrs={'class':'form-control'}),
        'isbn':forms.TextInput(attrs={'class':'form-control'}),
    }