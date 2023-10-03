from django import forms
from django.forms import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


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

    username = forms.CharField(min_length=4, max_length=25, widget=forms.TextInput())
    password = forms.CharField(min_length=5, widget=forms.PasswordInput())
    email = forms.EmailField(widget=forms.EmailInput())

    def clean_username(self):

        username = self.cleaned_data["username"]

        try:
            if User.objects.get(username=username):

                raise ValidationError("! غیر قابل استفاده")

        except User.DoesNotExist:

            return username.lower()

    def clean_email(self):

        email = self.cleaned_data["email"]

        try:
            if User.objects.get(email=email):

                raise ValidationError("! غیر قابل استفاده")

        except User.DoesNotExist:

            return email
