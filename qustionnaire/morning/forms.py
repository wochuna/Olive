from django import forms
from .models import Client

class MyForm(forms.ModelForm):
    class Meta:
        model = Client  # Specify the model to use
        fields = ['field1', 'field2']  # List the fields to include in the form