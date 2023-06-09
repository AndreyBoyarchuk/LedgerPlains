from django import forms
from .models import Ledger

class LedgerForm(forms.ModelForm):
    class Meta:
        model = Ledger
        fields = ['transaction_date', 'description', 'amount']
