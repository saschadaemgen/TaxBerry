from django.db import models
from django.utils import timezone
from decimal import Decimal
from core.models import Company


class Account(models.Model):
    ACCOUNT_TYPES = [
        ('asset', 'Aktiva'),
        ('liability', 'Passiva'),
        ('equity', 'Eigenkapital'),
        ('revenue', 'Erlöse'),
        ('expense', 'Aufwendungen'),
    ]
    
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='accounts')
    account_number = models.CharField(max_length=20, verbose_name='Kontonummer')
    name = models.CharField(max_length=200, verbose_name='Kontoname')
    account_type = models.CharField(max_length=50, choices=ACCOUNT_TYPES)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal('0.00'))
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        db_table = 'accounts'
        verbose_name = 'Konto'
        verbose_name_plural = 'Konten'
        unique_together = ['company', 'account_number']
        
    def __str__(self):
        return f"{self.account_number} - {self.name}"


class Transaction(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='transactions')
    date = models.DateField(verbose_name='Datum')
    description = models.TextField(verbose_name='Beschreibung')
    reference = models.CharField(max_length=100, blank=True, verbose_name='Referenz')
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey('accounts.User', on_delete=models.PROTECT)
    
    class Meta:
        db_table = 'transactions'
        verbose_name = 'Buchung'
        verbose_name_plural = 'Buchungen'
        
    def __str__(self):
        return f"{self.date} - {self.description[:50]}"