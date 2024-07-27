from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.utils import timezone

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    role = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.email
    
class Entreprise(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    company_name = models.CharField(max_length=255)
    website = models.URLField(null=True, blank=True)
    curiosityPass = models.BooleanField(default=False)
    WebDataPass = models.BooleanField(default=False)
    companyInformation = models.TextField(blank=True)
    nombreCDC = models.IntegerField(default=0)
    
    def __str__(self):
        return self.company_name
    
    
class Freelance(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    skills = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.user.first_name}-{self.skills}"