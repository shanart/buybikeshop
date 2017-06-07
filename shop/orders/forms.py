from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city' ]
        widgets={
            "first_name": forms.TextInput(attrs={
                'placeholder':'First name',
                'class':'form-control'
            }),
            "last_name": forms.TextInput(attrs={
                'placeholder':'Last name',
                'class':'form-control'
            }),
            "email" : forms.TextInput(attrs={
                'placeholder':'Email',
                'class':'form-control'
            }),
            "address" : forms.TextInput(attrs={
                'placeholder':'Address',
                'class':'form-control'
            }),
            "postal_code" : forms.TextInput(attrs={
                'placeholder':'Postal code',
                'class':'form-control'
            }),
            "city" : forms.TextInput(attrs={
                'placeholder':'City',
                'class':'form-control'
            })
        }
