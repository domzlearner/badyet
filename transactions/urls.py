from django.urls import path
from . import views

app_name = 'transactions'

urlpatterns = [
    path('add_transaction/', views.add_transaction, name='add_transaction'),
    path('transaction_list/<int:user_id>/', views.transaction_list, name='transaction_list'),
]