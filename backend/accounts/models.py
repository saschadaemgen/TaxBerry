from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    language = models.CharField(
        max_length=5, 
        default='de', 
        choices=[
            ('de', 'Deutsch'),
            ('en', 'English'),
        ]
    )
    company = models.ForeignKey(
        'core.Company', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True,
        related_name='users'
    )
    
    class Meta:
        db_table = 'users'
        verbose_name = 'Benutzer'
        verbose_name_plural = 'Benutzer'