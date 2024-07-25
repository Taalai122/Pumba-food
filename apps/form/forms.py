from django import forms
from .models import *


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=200, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = ContactUs
        fields = ('name','email','phone','message')



class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ваше имя', 'required': True}),
            'email': forms.EmailInput(attrs={'placeholder': 'Ваш email', 'required': True}),
            'phone': forms.TextInput(attrs={'placeholder': 'Ваш телефон', 'required': True}),
            'message': forms.Textarea(attrs={'placeholder': 'Ваше сообщение', 'required': True}),
        }
        error_messages = {
            'name': {
                'required': 'Это поле обязательно для заполнения.',
                'invalid': 'Введите корректное имя.',
            },
            'email': {
                'required': 'Это поле обязательно для заполнения.',
                'invalid': 'Введите корректный email.',
            },
            'phone': {
                'required': 'Это поле обязательно для заполнения.',
                'invalid': 'Введите корректный телефон.',
            },
            'message': {
                'required': 'Это поле обязательно для заполнения.',
                'min_length': 'Сообщение слишком короткое.',
            },
        }
