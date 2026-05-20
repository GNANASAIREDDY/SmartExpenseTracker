from django.db import models
from django.contrib.auth.models import User


class Income(models.Model):
    PAYMENT_CHOICES = (
        ('Cash', 'Cash'),
        ('UPI', 'UPI'),
        ('Bank', 'Bank'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.source} - {self.amount}"