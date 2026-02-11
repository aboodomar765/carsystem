from django import forms
from django.contrib.auth.models import User
from .models import Car, Sale, MonthlyExpense


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'car_type', 'year', 'chassis_number', 'purchase_date', 
                  'purchase_value', 'clearance_type']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'car_type': forms.Select(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'chassis_number': forms.TextInput(attrs={'class': 'form-control'}),
            'purchase_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'purchase_value': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'clearance_type': forms.Select(attrs={'class': 'form-control'}),
        }


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['sale_date', 'sale_value', 'partial_profit']
        widgets = {
            'sale_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'sale_value': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'partial_profit': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }


class MonthlyExpenseForm(forms.ModelForm):
    class Meta:
        model = MonthlyExpense
        fields = ['description', 'amount', 'date']
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
