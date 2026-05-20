from django import forms
from .models import Budget


class BudgetForm(forms.ModelForm):

    class Meta:
        model = Budget

        fields = [
            'category',
            'amount'
        ]

        widgets = {

            'category': forms.Select(attrs={
                'class': 'form-control'
            }),

            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Budget Amount'
            }),

        }