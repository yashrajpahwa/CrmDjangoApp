# imports
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import *
from django.contrib.auth.models import *

# main code


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['delete']


class customerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class productForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class createUserForm(UserCreationForm):
    username = forms.CharField(label='Username')
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Email Address')
    password1 = forms.CharField(label='Password')
    password2 = forms.CharField(label='Re-enter Password')

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name',
                  'username', 'password1', 'password2']
