from django.forms import ModelForm
from main.models import Books

class ProductForm(ModelForm):
    class Meta:
        model = Books
        fields = ["name", "amount", "description"]
