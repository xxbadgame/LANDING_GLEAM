from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Freelance, Entreprise

class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password1','password2']
        
class EntrepriseForm(forms.ModelForm):
    class Meta:
        model = Entreprise
        fields = ['company_name', 'website']
        
class FreelanceForm(forms.ModelForm):
    class Meta:
        model = Freelance
        fields = ['skills']