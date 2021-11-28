from django import forms
from . models import Homeworks


class AddHomeworkForm(forms.ModelForm):
    class Meta:
        model = Homeworks
        fields = (
            'subject',
            'text',
            'group',
            'date',
        )

