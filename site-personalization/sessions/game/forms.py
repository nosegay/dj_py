from django import forms


class NumberForm(forms.Form):
    number = forms.IntegerField(label='Введите число')
