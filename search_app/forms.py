from django import forms
from .models import TextFile

class DocumentForm(forms.ModelForm):
    class Meta:
        model = TextFile
        fields = ('content', )