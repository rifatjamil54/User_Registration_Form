from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class SingUp_Forms(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class UserEditForms(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "date_joined", "last_login"] 
        labels = {'emaill':'Email Address'}

class AdminEditForms(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = '__all__'
        labels = {'emaill':'Email Address'}        