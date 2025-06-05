from core.models import *
from django import forms
from django.forms import ModelForm, TextInput, DateInput, Select, CheckboxInput, Textarea,SelectMultiple
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StaffForm(ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'
        exclude = ['user','supervisor','status']
        widgets = {
            'Phone':forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'dept':forms.TextInput(attrs={
                'class': 'form-control'
            })
        }

class TaskForm(ModelForm):
    class Meta:
        model= Task
        fields = '__all__'
        exclude= ['status','up_date','created_date']
        widgets = {
            'title':forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'description':forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'assigned_to':forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'priority':forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }

class SanitizationReportForm(ModelForm):
    class Meta:
        model = SanitizationReport
        fields = '__all__'
        exclude = ['reporter_user', 'created_date', 'status']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 1
            }),
            'category': Select(attrs={
                'class': 'form-select'
            }),
            'reporter_name': TextInput(attrs={
                'class': 'form-control'
            }),
            'report': forms.TextInput(attrs={
                'class': 'form-control',
                'rows':3
            }),
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']