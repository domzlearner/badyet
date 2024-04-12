from .models import Transaction
from django import forms

# class IncomeForm(forms.ModelForm):
#     class Meta:
#         model = Income
#         fields = ['amount', 'date', 'category', 'description', 'savings_goal']

# class ExpenseForm(forms.ModelForm):
#     class Meta:
#         model = Expense
#         fields = ['amount', 'date', 'category', 'description', 'payment_method', 'is_recurring']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['name', 'amount', 'date', 'category', 'description']