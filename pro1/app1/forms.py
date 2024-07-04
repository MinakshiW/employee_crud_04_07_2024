from django import forms
from .models import Employee

gen = [('male', 'Male'),
       ('female', 'Female')]


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

        labels = {
            'eid' : 'Employeen ID',
            'name' : 'Employee Name',
            'email' : 'Email ID',
            'dob' : 'Birth Date',
            'gender' : 'Gender',
            'profile_pic' : 'Profile Picture'
        }

        widgets = {
            'eid' : forms.NumberInput(attrs={'class': 'form-control'}),
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control'}),
            'dob' : forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'gender' : forms.RadioSelect(choices=gen),
            'profile_pic' : forms.ClearableFileInput(attrs={'class': 'form-control'})
        }