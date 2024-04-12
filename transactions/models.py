from django.db import models
from django.contrib.auth.models import User
# from goals.models import Goal

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    name = models.CharField(max_length=100, default='Sample Transaction')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
# class Income(Transaction):
#     savings_goal = models.ForeignKey(Goal, on_delete=models.SET_NULL, blank=True, null=True)