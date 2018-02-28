from django import forms
from .models import pictures
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

class CaptchaTestForm(forms.Form):
	captcha =CaptchaField()
	    
class picturesForm(forms.ModelForm):

    class Meta:
        model = pictures
        fields = ['caption', 'images']



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
