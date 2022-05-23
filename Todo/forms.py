from dataclasses import field
from django import forms
from .models import Tasks

from crispy_forms.helper import FormHelper


class TodoForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'description', 'status']

        widgets = {
            'title' : forms.Textarea(attrs={'rows':1, 'cols':10}),
            'description' : forms.Textarea(attrs={'rows':4, 'cols':10}),
        }

    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        self.fields['status'].empty_lebel = "Select"
