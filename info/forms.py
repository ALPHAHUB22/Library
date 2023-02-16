from django import forms
from .models import Library, Userinfo

class Register(forms.Form):
    
    GENDER = (
        (1, "Male"),
        (2, "Female"),
        (3, "Other")
    )
    user = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    gender = forms.ChoiceField(choices=GENDER, widget=forms.RadioSelect())