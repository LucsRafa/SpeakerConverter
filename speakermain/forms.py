from django import forms
from .models import SpeakFile
from django.contrib.auth.models import User

class formSpeakFile (forms.ModelForm):
    class Meta:
        model = SpeakFile
        fields = ['titulo','corpo','modelo','formato']

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Senha")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirme a senha")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("As senhas não coincidem.")