from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name')

class LoginForm(forms.Form):
    identifier = forms.CharField(label='username/email')
    password = forms.CharField(widget=forms.PasswordInput)

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)