from django.shortcuts import render, redirect
from .models import Ledger
from .forms import LedgerForm

def home(request):
    if request.method == "POST":
        form = LedgerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LedgerForm()

    ledgers = Ledger.objects.all()
    return render(request, 'main/home.html', {'ledgers': ledgers, 'form': form})
