from django import forms
from .models import Thing


class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ["name", "description"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Enter name of thing"}),
            "description": forms.Textarea(
                attrs={"placeholder": "Enter description of thing"}
            ),
        }
