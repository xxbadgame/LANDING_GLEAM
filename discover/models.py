from django.db import models
from accounts.models import Entreprise

class Conversation(models.Model):
    company = models.ForeignKey(Entreprise, on_delete=models.CASCADE, related_name='conversations')
    conversation_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation {self.id} for {self.company.company_name}"