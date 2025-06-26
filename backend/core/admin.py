from django.contrib import admin
from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'tax_id', 'vat_id', 'created_at')
    search_fields = ('name', 'tax_id', 'vat_id')
    readonly_fields = ('created_at', 'updated_at')