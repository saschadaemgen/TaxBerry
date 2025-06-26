from django.contrib import admin
from .models import Account, Transaction


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_number', 'name', 'account_type', 'balance', 'company')
    list_filter = ('account_type', 'company')
    search_fields = ('account_number', 'name')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('date', 'description', 'reference', 'company', 'created_by')
    list_filter = ('date', 'company')
    search_fields = ('description', 'reference')
    date_hierarchy = 'date'