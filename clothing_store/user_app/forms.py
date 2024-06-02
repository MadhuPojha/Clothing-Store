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
    password = forms.CharField(
        max_length=30,
        widget=forms.PasswordInput(attrs={'class': 'form-control form-label', 'placeholder': 'Enter password'})
    )
    #password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):

    profile_pic = forms.ImageField(
        required=False, 
        widget=forms.FileInput(attrs={'class': 'form-control form-label'})
    )
    class Meta():
        model = UserProfileInfo
        fields = ( 'profile_pic',)

class AddressForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control form-label', 'placeholder': 'Enter first name'})
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control form-label', 'placeholder': 'Enter last name'})
    )
    street = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control form-label', 'placeholder': 'Enter street'})
    )
    city = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control form-label', 'placeholder': 'Enter city'})
    )
    state = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control form-label', 'placeholder': 'Enter state'})
    )
    zip_code = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control form-label', 'placeholder': 'Enter zip code'})
    )
    phone_number = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control form-label', 'placeholder': 'Enter phone number'})
    )
    class Meta():
        model = Address
        fields = ('first_name', 'last_name', 'street', 'city', 'state', 'zip_code', 'phone_number')

class UserPaymentInfoForm(forms.ModelForm):
    name_on_card = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control form-label', 'placeholder': 'Enter name on card'})
    )
    surname_on_card = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control form-label', 'placeholder': 'Enter surname on card'})
    )
    card_number = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control form-label', 'placeholder': 'Enter card number'})
    )
    expiration_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control form-label', 'placeholder': 'Enter expiration date'})
    )
    cvv = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control form-label', 'placeholder': 'Enter cvv'})
    )
    class Meta():
        model = UserPaymentInfo
        fields = ('name_on_card', 'surname_on_card', 'card_number', 'expiration_date', 'cvv')

class UserShippingInfoForm(forms.ModelForm):
    class Meta():
        model = UserShippingInfo
        fields = ('address',)

class UserBillingInfoForm(forms.ModelForm):
    class Meta():
        model = UserBillingInfo
        fields = ('address',)