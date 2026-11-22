from django import forms
from .models import UserProfile


class NameForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Введите ваше имя',
            })
        }
        labels = {
            'name': 'Ваше имя',
        }
