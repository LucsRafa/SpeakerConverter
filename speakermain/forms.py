from django import forms
from .models import SpeakFile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages

class formSpeakFile(forms.ModelForm):
    class Meta:
        model = SpeakFile
        fields = ['titulo', 'corpo', 'modelo', 'formato']


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password1')
        confirm_password = cleaned_data.get('password2')

        if password != confirm_password:
            raise forms.ValidationError("As senhas não coincidem.")
