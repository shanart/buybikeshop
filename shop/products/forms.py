from django import forms
from .models import Product, Wishlist

class AddToWishlistForm(forms.Form):
    item = forms.CharField(widget=forms.HiddenInput())
    user = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Wishlist
        fields = ['item', 'user']
