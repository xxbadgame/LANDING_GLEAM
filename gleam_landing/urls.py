from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from discover.views import *
from accounts.views import *

urlpatterns = [
    path('', index, name='index'),
    path('entreprises/', entreprises, name="entreprises"),
    path('votre-projet/', BotCreationProjet, name="BotCreationProjet"),
    path('freelances/', freelances, name="freelances"),
    path('histoire/', histoire, name="histoire"),
    
    #connexion et inscription
    path('admin/', admin.site.urls),
    path('connexion/', connexion, name="connexion"),
    path('inscriptionFreelances/', inscriptionFreelances, name="inscriptionFreelances"),
    path('inscriptionEntreprises/', inscriptionEntreprises, name="inscriptionEntreprises"),
    path('qui-etes-vous/', qui, name='qui'),
    path('profil/', profil, name='profil'),
    path('deconnexion/', deconnexion, name='logout'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
