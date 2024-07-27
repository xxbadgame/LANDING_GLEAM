from django.contrib import admin
from .models import CustomUser, Entreprise, Freelance

admin.site.register(CustomUser)
admin.site.register(Entreprise)
admin.site.register(Freelance)