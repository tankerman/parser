from django import forms
from .models import *

class AddressForm(forms.ModelForm):
    
    class Meta:
        model = Address
#         fields = ('__all__')
        exclude = ['info']
        
class SearchForm(forms.Form):
    field = forms.CharField(required=False, label='Поиск по несущим стенам')