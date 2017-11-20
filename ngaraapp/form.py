from django import forms
from ngaraapp.models import Contact
from ngaraapp.models import Service

# from ngaraapp.models import Login
import datetime

class ContactForm(forms.ModelForm):
    firstName = forms.CharField()
    lastName  = forms.CharField()
    email     = forms.EmailField()
    password  = forms.CharField(widget=forms.PasswordInput)  
    Location  = forms.CharField()
    

    class Meta:
          model = Contact
          fields = ('firstName', 'lastName', 'email', 'password',   'Location',)
          

class ServiceForm(forms.ModelForm):
    Name = forms.CharField()
    email     = forms.EmailField()
    # PhoneNumber =forms.CharField(max_length = 20)
    # password  = forms.CharField(widget=forms.PasswordInput)  
    location  = forms.CharField()

    
    
    class Meta:
          model = Service
          fields = ('Name',  'email','location')
          


# class LoginForm(forms.ModelForm):
#     EnterName        = forms.CharField()
#     EnterEmail       = forms.EmailField()
    
    

#     class Meta:
#           model = Login
#           fields = ('EnterName', 'EnterEmail')











# class ContactForm(forms.ModelForm):
#     firstName = forms.CharField()
#     lastName  = forms.CharField()
#     email     = forms.EmailField()
#     password  = forms.CharField(widget=forms.PasswordInput)  
#     estate    = forms.CharField()
#     Location  = forms.CharField()
    

#     class Meta:
#           model = Contact
#           fields = ('firstName', 'lastName', 'email', 'password',  'estate', 'Location',)


