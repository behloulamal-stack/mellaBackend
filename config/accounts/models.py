from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('client', 'زبون'),
        ('merchant', 'تاجر'),
        ('admin', 'ادمن'),
    )
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10, unique=True ,blank= True ,null=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='client')
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    
    
    REQUIRED_FIELDS = ['username',] 

    def __str__(self):
        return f"{self.username} - {self.role}"