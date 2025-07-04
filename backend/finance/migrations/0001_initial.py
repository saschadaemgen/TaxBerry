# Generated by Django 5.2.3 on 2025-06-26 15:54

import django.db.models.deletion
import django.utils.timezone
from decimal import Decimal
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Datum')),
                ('description', models.TextField(verbose_name='Beschreibung')),
                ('reference', models.CharField(blank=True, max_length=100, verbose_name='Referenz')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='core.company')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Buchung',
                'verbose_name_plural': 'Buchungen',
                'db_table': 'transactions',
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=20, verbose_name='Kontonummer')),
                ('name', models.CharField(max_length=200, verbose_name='Kontoname')),
                ('account_type', models.CharField(choices=[('asset', 'Aktiva'), ('liability', 'Passiva'), ('equity', 'Eigenkapital'), ('revenue', 'Erlöse'), ('expense', 'Aufwendungen')], max_length=50)),
                ('balance', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=15)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='core.company')),
            ],
            options={
                'verbose_name': 'Konto',
                'verbose_name_plural': 'Konten',
                'db_table': 'accounts',
                'unique_together': {('company', 'account_number')},
            },
        ),
    ]
