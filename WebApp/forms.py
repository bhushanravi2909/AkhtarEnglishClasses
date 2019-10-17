from django import forms
from WebApp.models import std_reg

class StdForm(forms.ModelForm):
    class Meta:
        model=std_reg
        fields='__all__'
