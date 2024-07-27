from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Freelance, Entreprise

class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password1','password2'] 
        labels={
        'first_name': 'Prénom',
        'last_name': 'Nom',
        }
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Entrez votre email'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Entrez votre prénom'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Entrez votre nom'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.label_suffix = ''
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Entrez votre mot de passe'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Entrez votre mot de passe à nouveau'})
                
                
class EntrepriseForm(forms.ModelForm):
    class Meta:
        model = Entreprise
        fields = ['company_name', 'website']
        labels={
        'company_name': "Nom de l'entreprise",
        'website': 'site web',
        }
        widgets = {
            'company_name': forms.TextInput(attrs={'placeholder': 'Entrez le nom de votre entreprise'}),
            'website': forms.TextInput(attrs={'placeholder': '(Si vous avez un site web)'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(EntrepriseForm, self).__init__(*args, **kwargs)
        self.label_suffix = ''
        
            
class FreelanceForm(forms.ModelForm):
    class Meta:
        model = Freelance
        fields = ['skills']
        labels={
            'skills': 'Votre spécialité informatique',
        }
        widgets = {
            'skills': forms.TextInput(attrs={'placeholder': 'Entrez votre spécialité ici'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(FreelanceForm, self).__init__(*args, **kwargs)
        self.label_suffix = ''
        
        
class ConnexionForm(forms.Form):
    email = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'Entrez votre email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Entrez votre mot de passe'}), required=True)
    
    def __init__(self, *args, **kwargs):
        super(ConnexionForm, self).__init__(*args, **kwargs)
        self.label_suffix = ''

    