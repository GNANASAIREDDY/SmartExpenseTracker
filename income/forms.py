from django import forms
from .models import Income


class IncomeForm(forms.ModelForm):

    class Meta:
        model = Income

        fields = [
            'source',
            'amount',
            'description'
        ]

        widgets = {

            'source': forms.Select(attrs={
                'class': 'form-control'
            }),

            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Amount'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Description',
                'rows': 3
            }),
        }