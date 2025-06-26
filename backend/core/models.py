from django.db import models
from django.utils import timezone

class Company(models.Model):
    name = models.CharField(max_length=200, verbose_name='Firmenname')
    tax_id = models.CharField(max_length=50, verbose_name='Steuernummer')
    vat_id = models.CharField(max_length=50, blank=True, verbose_name='USt-IdNr.')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'companies'
        verbose_name = 'Unternehmen'
        verbose_name_plural = 'Unternehmen'
        
    def __str__(self):
        return self.name