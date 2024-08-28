# accounts/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import ConsumptionRecord


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Логин', max_length=150)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class ConsumptionRecordForm(forms.ModelForm):
    class Meta:
        model = ConsumptionRecord
        fields = ['date', 'kwh_consumed', 'tariff']

from django import forms

class ConsumerSearchForm(forms.Form):
    name = forms.CharField(max_length=100, required=False, label='Никнейм')
