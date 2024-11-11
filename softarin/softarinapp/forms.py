from django import forms
from .models import *
from captcha.fields import CaptchaField
from django.utils.translation import gettext_lazy as _
from django.forms.widgets import TextInput

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Contact
        fields = ['contact_name', 'contact_phone', 'contact_email']
        widgets = {
            'contact_name': forms.TextInput(attrs={
                'class': 'feed-back-feld_in', 
                'size': '40', 
                'autocomplete': 'name', 
                'aria-required': 'true', 
                'aria-invalid': 'false',
                'placeholder': _('NAME')
            }),
            'contact_phone': forms.TextInput(attrs={
                'class': 'feed-back-feld_in', 
                'size': '40', 
                'autocomplete': 'name', 
                'aria-required': 'true', 
                'aria-invalid': 'false',
                'placeholder': _('PHONE')
            }),
            'contact_email': forms.TextInput(attrs={
                'class': 'feed-back-feld_in', 
                'size': '40', 
                'autocomplete': 'name', 
                'aria-required': 'true', 
                'aria-invalid': 'false',
                'placeholder': _('E-MAIL')
            }),
        }