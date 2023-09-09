from django import forms
from django.forms import ValidationError
from django.contrib.auth import authenticate


class LoginForm(forms.Form):

    username = forms.CharField(min_length=2, widget=forms.TextInput(attrs={
        "class": "input100",
        "placeholder": "یوزرنیم را وارد کنید",
        "style": "text-align:center"
    }))

    password = forms.CharField(min_length=2, widget=forms.PasswordInput(attrs={
        "class": "input100",
        "placeholder": "پسورد را وارد کنید",
        "style": "text-align:center"
    }))

    def clean(self):

        cleaned_data = super().clean()

        username = cleaned_data["username"]
        password = cleaned_data["password"]

        user = authenticate(username=username, password=password)

        if user is None:
            raise ValidationError("! یوزرنیم یا پسورد اشتباه است")


class RegisterForm(forms.Form):
    pass

