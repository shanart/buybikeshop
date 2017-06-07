from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )

from .models import Profile
User = get_user_model()

class UserLoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect passsword")
            if not user.is_active:
                raise forms.ValidationError("This user is not longer active.")
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Username'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Email'}))
    email2 = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Confirm email'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Password'}))

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password'
        ]

    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Emails must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email has already been registered")
        return email

class UpdateProfile(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Username'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Email'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Last name'}))

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]

class ProfileForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Bio'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Location'}))
    age = forms.CharField(widget=forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder':'Age',
                'min': '0',
                'max': '100',
                'step': '1'})
            )
    userpic =  forms.FileInput()

    class Meta:
        model = Profile
        fields = ['bio', 'location', 'age', 'userpic' ]
