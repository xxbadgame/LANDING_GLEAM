from django.shortcuts import render
from .AssistantAI.Assistant import *
from django.http import HttpResponse
from accounts.models import Entreprise
from discover.models import CahierDeCharge, Tache
import os
import json


def index(request):
    return render(request, 'discover/index.html')

def entreprises(request):
    user = request.user
    entreprise = Entreprise.objects.get(user=user)
    curiostyPassValidation = entreprise.curiosityPass
    return render(request, 'discover/entreprises.html', context={'curiostyPassValidation': curiostyPassValidation})

def projects(request):    
    user = request.user
    entreprise = Entreprise.objects.get(user=user)
    curiostyPassValidation = entreprise.curiosityPass
    return render(request,'discover/choixProjet.html', context={'curiostyPassValidation': curiostyPassValidation})

def rovers(request):
    thread = create_thread()
    request.session['thread_id'] = thread.id
    
    path_url = request.path
    print(path_url)
    user = request.user
    entreprise = Entreprise.objects.get(user=user)
    
    persoPretty = ''
    sujetFR = ''
    sujetEN = ''
    
    if entreprise.curiosityPass == False:
        persoPretty = 'Curiosity'
        sujetFR = 'entreprise'
        sujetEN = 'business'
    if 'projects' in path_url and entreprise.curiosityPass:
        persoPretty = 'Perseverance'
        sujetFR = 'cahier des charges'
        sujetEN = 'specifications'
    if 'visions' in path_url and entreprise.curiosityPass:
        persoPretty = 'Opportunity'
        sujetFR = 'avancement WEB et DATA'
        sujetEN = 'WEB and DATA advancement'

    
    return render(request, 'discover/rovers.html', context={'personality':persoPretty,'sujetFR':sujetFR,'sujetEN':sujetEN, "path_url":path_url})


def freelances(request):
    return render(request, 'discover/freelances.html')

def histoire(request):
    return render(request, 'discover/histoire.html')


def roversPersonality(request, project=None):
    
    # Récuperer les infos users et entreprise en BDD
    user = request.user
    entreprise = Entreprise.objects.get(user=user)
    contexteEntreprise = entreprise.companyInformation
    
    # personnalité de l'IA
    personality = ''

    # contexte envoyé à l'IA
    contexteEntrepriseSend = False
    
    # Choix de la personnalité selon le parcours
    
    path_url = request.META.get('HTTP_REFERER')
    print("chemin :",path_url)
    if entreprise.curiosityPass == False:
        personality = 'AI_CURIOSITY'
    elif 'Perseverance' in path_url and entreprise.curiosityPass == True:
        personality = 'AI_PERSEVERANCE'
        print("AI_PERSEVERANCE")
    elif 'Opportunity' in path_url and entreprise.curiosityPass == True:
        personality = 'AI_OPPORTUNITY'
        print("AI_OPPORTUNITY")
    else:
        print("pas de personalité")

    print("personality : ", personality)
    
    # execution thread et de l'assistant
    thread_id = request.session.get('thread_id', None)
    ASSISTANT_ID = os.environ.get(personality)
    assistant = retrieve_assistant(ASSISTANT_ID)
    
    # Réception message, traitement et renvoie au front
    if request.method == "POST":
        
        # Ajout du message pour l'assistant pour le contexte
        if personality == 'AI_OPPORTUNITY' or personality == 'AI_PERSEVERANCE':
            if contexteEntrepriseSend == False:
                Add_message(message=contexteEntreprise, thread_id=thread_id)
                contexteEntrepriseSend = True  
            if personality == 'AI_PERSEVERANCE':
                # Edit pour adapter le projet au carousel
                Add_message(message="data collecte de donnée", thread_id=thread_id)
                 

        # Message de l'utilisateur
        message = request.POST.get('message')
        print(message)
        Add_message(message=message, thread_id=thread_id)
        
        # Réponse OPEN AI numero 1 avec base CDC
        responseJSON = run_assistant(assistant=assistant, thread_id=thread_id)
        respPyJSONfirst =  json.loads(responseJSON)
        status = respPyJSONfirst["status"]
        print("JSON réponse : ",responseJSON)
  
         # Fin de process
        if status == 'finProcessCuriosity':
            
            companyInformationResponse = respPyJSONfirst['companyInformation']
            entreprise.companyInformation = companyInformationResponse
            entreprise.curiosityPass = True
            entreprise.save()
        
        elif status == 'finProcessAll':
            print("dedans")
            ###### L'utilisation de SPIRIT plus tard ######
            # completion du CDC avec les prix et renvoie du json complet
            #personalitySwitch = 'AI_SPIRIT'
            #ASSISTANT_ID = os.environ.get(personalitySwitch)
            #assistant = retrieve_assistant(ASSISTANT_ID)
            #Add_message(message=f"Ajoute dans ce JSON {responseJSON} de base les prix pour des freelance Junior pour GLEAM et senior pour la concurrence", thread_id=thread_id)
            #responseJSON = run_assistant(assistant=assistant, thread_id=thread_id)
            #respPyJSON =  json.loads(responseJSON)
            #print(respPyJSON)
            ##############################################

            # Ajout des infos projets dans la BDD
            for projet in respPyJSONfirst["projets"]:
                cdc = projet['cahierDesCharges']
                creaCDC= CahierDeCharge.objects.create(
                    user = entreprise,
                    titre = cdc["titre"],
                    description = cdc["description"],
                    noteCohereneEntreprise = int(cdc['noteSur100']),
                    justificationNote = cdc["justificationNote"],
                    tempsProjet = cdc["tempsProjet"],
                    prixGlobal = int(cdc["prixGlobal"]),
                    prixGlobalConcurrents = int(cdc["prixGlobalConcurrents"])
                )
                
                creaCDC.save()
                entreprise.nombreCDC += 1
                entreprise.save()
                
                if personality == 'AI_PERSEVERANCE':
                    for tache in cdc["taches"]:
                        creaTache = Tache.objects.create(
                            CahierDeCharge = creaCDC,
                            titreTache = tache["titreTache"],
                            poste = tache["posteTache"],
                            descriptionTache = tache["descriptionTache"],
                            tempsTache = tache["tempsTache"],
                            prixTache = tache["prixTache"],
                            prixTacheConcurrents = tache["prixTacheConcurrents"]
                        )
                        
                        creaTache.save()
            
        return HttpResponse(responseJSON)
        
    return render(request, 'discover/rovers.html')


def pricingOpportunity(request):
    user = request.user
    entreprise = Entreprise.objects.get(user=user)
    cahiers_des_charges = CahierDeCharge.objects.filter(user=entreprise)
    
    context = {
        'entreprise': entreprise,
        'cahiers_des_charges': cahiers_des_charges,
    }
    return render(request, 'discover/pricingOpportunity.html', context)


def pricingPerseverance(request):
    user = request.user
    entreprise = Entreprise.objects.get(user=user)
    cahiers_des_charges = CahierDeCharge.objects.filter(user=entreprise).prefetch_related('taches')
    
    context = {
        'entreprise': entreprise,
        'cahiers_des_charges': cahiers_des_charges,
    }
    return render(request, 'discover/pricingPerseverance.html', context)