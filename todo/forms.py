# todo/forms.py

from django import forms
from django.contrib.auth.models import User
import re


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

    # 🔹 Username validation
    def clean_username(self):
        username = self.cleaned_data['username']

        if len(username) < 5:
            raise forms.ValidationError("Username must be at least 5 characters long.")

        if "_" not in username:
            raise forms.ValidationError("Username must contain '_' (e.g., first_last).")

        parts = username.split("_")
        if len(parts) != 2 or not all(parts):
            raise forms.ValidationError("Username must be in format first_last.")

        return username

    # 🔹 Password validation
    def clean_password(self):
        password = self.cleaned_data['password']

        if len(password) < 8 or len(password) > 12:
            raise forms.ValidationError("Password must be between 8 and 12 characters.")

        if not re.search(r'[a-z]', password):
            raise forms.ValidationError("Password must contain a lowercase letter.")

        if not re.search(r'[A-Z]', password):
            raise forms.ValidationError("Password must contain an uppercase letter.")

        if not re.search(r'\d', password):
            raise forms.ValidationError("Password must contain a number.")

        if not re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
            raise forms.ValidationError("Password must contain a special character.")

        return password 