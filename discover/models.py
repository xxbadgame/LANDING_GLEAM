from django.db import models
from accounts.models import Entreprise

class CahierDesCharges(models.Model):
    user = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    titre = models.CharField(max_length=50)
    description = models.TextField(null=False)
    
    def __str__(self):
        return f"Titre:{self.titre}-{self.description}"