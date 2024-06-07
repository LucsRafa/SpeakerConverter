from django import forms
from .models import SpeakFile

class formSpeakFile (forms.ModelForm):
    class Meta:
        model = SpeakFile
        fields = ['titulo','corpo','modelo','formato']
