from rest_framework import viewsets, permissions
from .models import Company
from .serializers import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        # Nutzer sehen nur ihre eigene Company
        if self.request.user.company:
            return Company.objects.filter(id=self.request.user.company.id)
        return Company.objects.none()