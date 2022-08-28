from django import forms
from .models import taskDb

class taskForm(forms.ModelForm):
    class Meta:
        model = taskDb
        fields = ['title','description','post']
