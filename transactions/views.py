from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Transaction
from .forms import TransactionForm

def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('transactions:transaction_list', user_id=request.user.id)
    else:
        form = TransactionForm()
    return render(request, 'transactions/add_transaction.html', {'form': form})

@login_required
def transaction_list(request, user_id):
    transactions = Transaction.objects.filter(user_id=user_id)
    return render(request, 'transactions/transaction_list.html', {'transactions': transactions})
