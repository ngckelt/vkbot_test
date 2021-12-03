from django import forms
from .models import Deadlines


class AddDeadlineForm(forms.ModelForm):
    class Meta:
        model = Deadlines
        fields = (
            'text',
            'group',
            'date',
        )

