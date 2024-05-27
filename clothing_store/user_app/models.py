from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username

class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    street  = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

class UserPaymentInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name_on_card = models.CharField(max_length=100)
    surname_on_card = models.CharField(max_length=100)
    card_number = models.CharField(max_length=16)
    expiration_date = models.DateField()
    cvv = models.CharField(max_length=3)

    def __str__(self):
        return self.user.username
