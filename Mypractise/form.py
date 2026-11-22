from django import forms
from .model import UserProfile

class NameForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        field = ['name']
        widget = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Введите свою имя'
            }
            )
        }