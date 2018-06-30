from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()


class GuestForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username',
            'style': 'margin-bottom: 5px; margin-right: 17px; margin-left: 6px',
        })
    )


class RegisterForm(forms.Form):

    username = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username',
            'style': 'margin-bottom: 5px; margin-right: 17px; margin-left: 6px',
        })
    )
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'example@example.com',
            'style': 'margin-bottom: 5px; margin-right: 17px; margin-left: 6px',
        }
    ))
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            # 'type': 'password',
            'style': 'margin-bottom: 5px; margin-right: 17px; margin-left: 6px',
        }
    ))
    password2 = forms.CharField(max_length=32, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Confirm Password',
            # 'type': 'password',
            'style': 'margin-bottom: 5px; margin-left: 6px',
        }
    ))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email taken. Choose another email address")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password2 != password:
            raise forms.ValidationError("Password didn't match")
        return data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username',
            'style': 'margin-bottom: 5px; margin-right: 17px; margin-left: 6px',
        }
    ))
    password = forms.CharField(max_length=32, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Confirm Password',
            'type': 'password',
            'style': 'margin-bottom: 5px; margin-left: 6px',
        }
    ))
