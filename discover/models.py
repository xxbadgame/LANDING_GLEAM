from django.db import models
from accounts.models import Entreprise
from django.utils import timezone

class CahierDeCharge(models.Model):
    user = models.ForeignKey(Entreprise, on_delete=models.CASCADE, related_name='cahiers_de_charge')
    titre = models.CharField(max_length=50)
    description = models.TextField(null=True)
    noteCohereneEntreprise = models.IntegerField(null=True) # Note sur 100
    justificationNote = models.TextField(null=True)
    tempsProjet = models.TextField(null=True)
    prixGlobal = models.IntegerField(null=True)
    prixGlobalConcurrents = models.IntegerField(null=True)
    discover = models.BooleanField(null=False)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.user}-{self.titre}"
    
class Tache(models.Model):
    CahierDeCharge = models.ForeignKey(CahierDeCharge, on_delete=models.CASCADE, related_name='taches')
    titreTache = models.CharField(max_length=50)
    poste = models.CharField(max_length=250)
    descriptionTache = models.TextField(null=True)
    tempsTache = models.TextField(null=True)
    prixTache = models.IntegerField(null=True)
    prixTacheConcurrents = models.IntegerField(null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.poste



    