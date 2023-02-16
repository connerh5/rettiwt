from django import forms
from .models import Rett

class RettForm(forms.ModelForm):
    body = forms.CharField(required=True,
            widget=forms.widgets.Textarea(
                attrs={
                    "placeholder": "Enter your Rett",
                    "class":"form-control",
                }
            ),
            label="",
            )
    class Meta:
        model= Rett
        exclude = ("user",)