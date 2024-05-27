from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo, UserPaymentInfo, Address, UserShippingInfo, UserBillingInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

class UserProfileInfoForm(forms.ModelForm):
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