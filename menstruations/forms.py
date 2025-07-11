from django import forms
from .models import Menstruation

class MenstruationForm(forms.ModelForm):
    class Meta:
        model = Menstruation
        fields = ('start','end',)