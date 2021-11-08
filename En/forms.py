from django import forms
from .models import *

class PracticeForm(forms.Form):
    name = forms.CharField(max_length=150,label="Name",widget= forms.TextInput(attrs={'style':'color:black;'}))
    surname = forms.CharField(max_length=150,label="Surname",widget= forms.TextInput(attrs={'style':'color:black;'}))
    jobs = forms.CharField(max_length=150,label="Job place",widget= forms.TextInput(attrs={'style':'color:black;'}))
    phone = forms.CharField(max_length=150,label="Phone",widget= forms.TextInput(attrs={'style':'color:black;'}))
    mail = forms.CharField(max_length=150,label="Mail",widget= forms.TextInput(attrs={'style':'color:black;'}))

class JoinusForm(forms.Form):
    name = forms.CharField(max_length=150,label="Name",widget= forms.TextInput(attrs={'style':'color:black;'}))
    surname = forms.CharField(max_length=150,label="Surname",widget= forms.TextInput(attrs={'style':'color:black;'}))
    jobs = forms.CharField(max_length=150,label="Jobs",widget= forms.TextInput(attrs={'style':'color:black;'}))
    phone = forms.CharField(max_length=150,label="Phone",widget= forms.TextInput(attrs={'style':'color:black;'}))
    mail = forms.CharField(max_length=150,label="Mail",widget= forms.TextInput(attrs={'style':'color:black;'}))