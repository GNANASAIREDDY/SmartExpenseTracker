from django import forms

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from .models import Profile


class RegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:

        model = User

        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]


class LoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        })
    )


class ProfileForm(forms.ModelForm):

    class Meta:

        model = Profile

        fields = [
            'bio',
            'profile_image'
        ]

        widgets = {

            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4
            }),

            'profile_image': forms.FileInput(attrs={
                'class': 'form-control'
            })

        }