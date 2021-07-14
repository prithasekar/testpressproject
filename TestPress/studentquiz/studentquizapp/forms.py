from django import forms
from studentquizapp.models import *
class QuestionForm(forms.ModelForm):
    class Meta:
        model=Question
        fields='__all__'
