from rest_framework import viewsets, permissions
from .models import Account, Transaction
from .serializers import AccountSerializer, TransactionSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        # Nutzer sehen nur Konten ihrer Company
        if self.request.user.company:
            return Account.objects.filter(company=self.request.user.company)
        return Account.objects.none()
    
    def perform_create(self, serializer):
        # Automatisch die Company des Users setzen
        serializer.save(company=self.request.user.company)


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        # Nutzer sehen nur Transaktionen ihrer Company
        if self.request.user.company:
            return Transaction.objects.filter(company=self.request.user.company)
        return Transaction.objects.none()
    
    def perform_create(self, serializer):
        # Automatisch Company und User setzen
        serializer.save(
            company=self.request.user.company,
            created_by=self.request.user
        )