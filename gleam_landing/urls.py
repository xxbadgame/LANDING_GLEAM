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
    path('entreprises/projects/', projects, name="projects"),
    path('entreprises/projects/rovers/Curiosity', rovers, name="projects-rovers-curiosity"),
    path('entreprises/visions/rovers/Curiosity', rovers, name="visions-rovers-curiosity"),
    path('entreprises/projects/rovers/Perseverance/', rovers, name="projects-rovers-perseverance"),
    path('entreprises/visions/rovers/Opportunity', rovers, name="visions-rovers-opportunity"),
    path('entreprises/projects/rovers/Perseverance/pricing', pricingPerseverance, name="projects-rovers-perseverance-pricing"),
    path('entreprises/visions/rovers/Opportunity/pricing', pricingOpportunity, name="visions-rovers-opportunity-pricing"),
    path('rovers-personality/', roversPersonality, name="roversPersonality"),
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
