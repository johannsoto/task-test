from django import forms
from django.forms import ModelForm
from .models import task

PRIORITY_CHOICES =(
    ("LOW", "low"),
    ("MEDIUM", "medium"),
    ("HIGH", "high"),
    )


class taskForm(ModelForm):
    class Meta:
        model = task
        
        
        fields = ('emp_priority', 'emp_task_name', 'emp_due_date', 'emp_description')

    
        emp_priority : forms.ChoiceField(choices = PRIORITY_CHOICES)

        widgets = {
            
            'emp_task_name': forms.TextInput(attrs={'class': 'form-center , text-center', 'placeholder': 'TASK NAME','style':'width:600px; border-radius:12px; border:1px solid; height:40px; border-color:#E6ECF8; padding: calc(0.75rem - 1px; '}),
            'emp_due_date': forms.TextInput(attrs={'class': 'form-center, text-center', 'placeholder': 'YYYY-MM-DD','style':'width:600px; border-radius:12px; border:1px solid; height:40px; border-color:#E6ECF8; padding: calc(0.75rem - 1px); '}),
            'emp_description': forms.TextInput(attrs={'class': 'form-center, text-center', 'placeholder': 'DESCRIPTION','style':' height:100px; Width:600px; border-radius:12px; border:1px solid; border-color:#E6ECF8; flex-direction:column; padding: calc(0.75rem - 1px); '}),
        }