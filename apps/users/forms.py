from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={
        'class':'forms-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'forms-control'
    }))
    class Meta:
        model=User
        fields=['username','password']

class RegistrationForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={
        'class':'forms-control'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
    }))

    class Meta:
        model=User
        fields=['username','password1','password2','email']
        widgets={
            'email':forms.EmailInput(attrs={
                'class': 'forms-control'
            })
        }
