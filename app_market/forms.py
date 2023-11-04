from django import forms
from .models import Client

class AddClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ("client_id","name","brokerage","date")
        widgets = {
            'client_id':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Client ID'}),
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name'}),
            'brokerage':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Brokerage'}),
            'date':forms.DateInput(attrs={'class':'form-control','placeholder':'Enter Date','type':'date'}),
        }

