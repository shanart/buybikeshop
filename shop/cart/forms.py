from django import forms

# PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(initial=1, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Quantity'}))
    update = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )
