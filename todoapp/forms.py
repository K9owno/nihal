from django import forms
from .import models

class todo(forms.ModelForm):
    class Meta:
        model = models.Todo
        fields={'text'}