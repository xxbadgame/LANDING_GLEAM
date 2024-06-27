from django.db import models
from accounts.models import Entreprise

class CahierDeCharge(models.Model):
    user = models.ManyToManyField(Entreprise, related_name="tache")
    titre = models.CharField(max_length=50)
    description = models.TextField(null=True)
    noteCohereneEntreprise = models.IntegerField(null=True) # Note sur 100
    justificationNote = models.TextField(null=True)
    tempsProjet = models.TextField(null=True)
    prixGlobale = models.IntegerField(null=True)
    prixGlobaleConcurrents = models.IntegerField(null=True)
    
    def __str__(self):
        return f"Titre:{self.titre}-{self.description}"
    
class Tache(models.Model):
    CahierDesCharges = models.ManyToManyField(CahierDeCharge, related_name="tache")
    titreTache = models.CharField(max_length=50)
    poste = models.CharField(max_length=250)
    descriptionTache = models.TextField(null=True)
    tempsTache = models.TextField(null=True)
    prixTache = models.IntegerField(null=True)
    prixTacheConcurrents = models.IntegerField(null=True)

    def __str__(self):
        return self.poste



    