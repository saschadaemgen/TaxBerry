from rest_framework import serializers
from .models import Account, Transaction
from decimal import Decimal


class AccountSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name', read_only=True)
    
    class Meta:
        model = Account
        fields = ['id', 'account_number', 'name', 'account_type', 
                  'balance', 'company', 'company_name', 'created_at']
        read_only_fields = ['id', 'balance', 'created_at', 'company_name']
        
    def validate_balance(self, value):
        if value < Decimal('0') and self.initial_data.get('account_type') in ['asset', 'expense']:
            raise serializers.ValidationError("Aktiv- und Aufwandskonten dürfen nicht negativ sein.")
        return value


class TransactionSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name', read_only=True)
    created_by_username = serializers.CharField(source='created_by.username', read_only=True)
    
    class Meta:
        model = Transaction
        fields = ['id', 'date', 'description', 'reference', 
                  'company', 'company_name', 'created_at', 
                  'created_by', 'created_by_username']
        read_only_fields = ['id', 'created_at', 'created_by', 
                           'company_name', 'created_by_username']