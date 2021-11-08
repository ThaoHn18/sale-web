from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.forms import Form



class RegisterForm(Form):
    first_name = forms.CharField(
        label='First name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'id':'first_name'
            }
        )
    )

    last_name = forms.CharField(
        label='Last name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'id':'last_name'
            }
        )
    )

    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'id':'username'
            }
        )
    )

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'id':'password'
            }
        )
    )

    confirm_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'id':'confirm_password'
            }
        )
    )

    email = forms.EmailField(
        label=" Email",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'id':'email'
            }
        )
    )

    # Validation: username, email,password, confirm password,

    def clean_username(self):
        inputed_username = self.cleaned_data['username']
        try:
            User.objects.get(username=inputed_username)
            raise ValidationError(f"{inputed_username} already exits")
        except User.DoesNotExist:
            return inputed_username
    def clean_email(self):
        inputed_email = self.cleaned_data['email']
        try:
            User.objects.get(email=inputed_email)
            raise ValidationError(f"{inputed_email} already exits")
        except User.DoesNotExist:
            return inputed_email

    def clean_confirm_password(self):
        inputed_password = self.cleaned_data['password']
        inputed_confirm_password = self.cleaned_data['confirm_password']
        if inputed_password != inputed_confirm_password:
            raise ValidationError(f"password incorect")
        return inputed_confirm_password

    def save_user(self):
        User.objects.create_user(
            username = self.cleaned_data['username'],
            password = self.cleaned_data['password'],
            email = self.cleaned_data['email'],
            first_name = self.cleaned_data['first_name'],
            last_name = self.cleaned_data['first_name']   
        )

class LoginForm(Form):
    username = forms.CharField(
        label="user name",
        widget=forms.TextInput(
            attrs={
                'class':'form_control',
                'id': 'username'
            }
        )
    )

    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'id':'password'
            }
        )
    )