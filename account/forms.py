from django import forms
from django.core.exceptions import ValidationError

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs= {
            'class':'form-control col col-sm-8',
            'placeholder':'First Name',
            'style': 'margin-bottom: 5px; margin-right: 17px; margin-left: 6px', 
            'id': 'user'
        }
    ))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs= {
            'class': 'form-control',
            'placeholder':'Last Name',
            'style': 'margin-bottom: 5px; margin-right: 17px; margin-left: 6px',
        }
    ))
    username = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs= {
            'class': 'form-control',
            'placeholder':'Username',
            'style': 'margin-bottom: 5px; margin-right: 17px; margin-left: 6px',
        }
    ))
    email = forms.EmailField(widget=forms.TextInput(
        attrs= {
            'class': 'form-control',
            'placeholder':'example@example.com',
            'style': 'margin-bottom: 5px; margin-right: 17px; margin-left: 6px',
        }
    ))
    password1 = forms.CharField(max_length=32, widget=forms.TextInput(
        attrs= {
            'class': 'form-control',
            'placeholder':'Password',
            'type': 'password',
            'style': 'margin-bottom: 5px; margin-right: 17px; margin-left: 6px',
        }
    ))
    password2 = forms.CharField(max_length=32, widget=forms.TextInput(
        attrs= {
            'class': 'form-control',
            'placeholder':'Confirm Password',
            'type': 'password',
            'style': 'margin-bottom: 5px; margin-left: 6px',
        }
    ))

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password2 != password1:
            raise ValidationError("Password didn't match")
            
        return password2

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs= {
            'class': 'form-control',
            'placeholder':'Username',
            'style': 'margin-bottom: 5px; margin-right: 17px; margin-left: 6px',
        }
    ))
    password = forms.CharField(max_length=32, widget=forms.TextInput(
        attrs= {
            'class': 'form-control',
            'placeholder':'Confirm Password',
            'type': 'password',
            'style': 'margin-bottom: 5px; margin-left: 6px',
        }
    ))