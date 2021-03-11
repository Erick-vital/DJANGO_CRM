from django.forms import ModelForm
from .models import Customer

class ClienteForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'email']