from django import forms
from .models import Books

class Forms(forms.ModelForm) :
    class Meta:
        model = Books
        fields = '__all__'
