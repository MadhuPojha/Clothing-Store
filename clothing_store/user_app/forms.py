from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo, UserPaymentInfo, Address, UserShippingInfo, UserBillingInfo

class UserForm(forms.ModelForm):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control form-label', 'placeholder': 'Enter user name'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control form-label', 'placeholder': 'Enter email'})
    )
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control form-label', 'placeholder': 'Enter first name'})
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control form-label', 'placeholder': 'Enter last name'})
    )
    password = forms.CharField(
        max_length=30,
        widget=forms.PasswordInput(attrs={'class': 'form-control form-label', 'placeholder': 'Enter password'})
    )
    #password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

class UserProfileInfoForm(forms.ModelForm):
    phone_number = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control form-label', 'placeholder': 'Enter phone number'})
    )
    address = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control form-label', 'placeholder': 'Enter Address'})
    )
    profile_pic = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control form-label'}))
    class Meta():
        model = UserProfileInfo
        fields = ('phone_number', 'address', 'profile_pic')

class UserPaymentInfoForm(forms.ModelForm):
    class Meta():
        model = UserPaymentInfo
        fields = ('name_on_card', 'surname_on_card', 'card_number', 'expiration_date', 'cvv')

class AddressForm(forms.ModelForm):
    class Meta():
        model = Address
        fields = ('first_name', 'last_name', 'street', 'city', 'state', 'zip_code', 'phone_number')

class UserShippingInfoForm(forms.ModelForm):
    class Meta():
        model = UserShippingInfo
        fields = ('address',)

class UserBillingInfoForm(forms.ModelForm):
    class Meta():
        model = UserBillingInfo
        fields = ('address',)