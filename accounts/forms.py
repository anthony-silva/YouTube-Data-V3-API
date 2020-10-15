from django import forms 
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterForm(forms.Form):
    email = forms.EmailField(
        widget = forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    first_name = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    last_name = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError('This is an invalid user.')
        return email


class LoginForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'user-password'
            }
        )
    )


    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError('This is an invalid username.')
        return username
