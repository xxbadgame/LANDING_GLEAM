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

    
    return render(request, 'discover/rovers.html', context={'personality':persoPretty,'sujetFR':sujetFR,'sujetEN':sujetEN})


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
    
    path_url = request.path
    print("chemin : ",path_url)
    if entreprise.curiosityPass == False:
        personality = 'AI_CURIOSITY'
    if 'projects' in path_url and entreprise.curiosityPass:
        personality = 'AI_PERSEVERANCE'
    if 'visions' in path_url and entreprise.curiosityPass:
        personality = 'AI_OPPORTUNITY'


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
                Add_message(message=project, thread_id=thread_id)
                 

        # Message de l'utilisateur
        message = request.POST.get('message')
        print(message)
        Add_message(message=message, thread_id=thread_id)
        
        # Réponse OPEN AI
        responseJSON = run_assistant(assistant=assistant, thread_id=thread_id)        
        print(responseJSON)
        respPyJSON =  json.loads(responseJSON)
        status = respPyJSON["status"]
        
        # Fin de process
        if personality == 'AI_CURIOSITY' and status == 'finProcess':
            companyInformationResponse = respPyJSON.get('companyInformation')
            entreprise.companyInformation = companyInformationResponse
            entreprise.curiosityPass = True
            
            
        elif personality == 'AI_OPPORTUNITY' or personality == 'AI_PERSEVERANCE' and status == 'finProcess':
            
            # Ajout des infos projets dans la BDD
            ListeCDC = respPyJSON["project"]
            for cdc in ListeCDC:
                
                if personality == 'AI_OPPORTUNITY':
                    # 12 fois car un CDC
                    personality = 'AI_SPIRIT'
                    # Add message pour prix global par CDC
                    # Add message concurrent pour meme CDC
                    
                    # réponse JSON sur les prix
                    
                elif personality == 'AI_PERSEVERANCE':
                    # 1 fois car un CDC
                    personality = 'AI_SPIRIT'
                    # Add message pour prix global par CDC
                    # Add message concurrent pour meme CDC
                    # Add message pour prix pour cette tache
                    # Add message concurrent pour meme tache
                    
                    # réponse JSON sur les prix
                    
                creaCDC= CahierDeCharge.objects.create(
                    user = entreprise,
                    titre = cdc["titre"],
                    description = cdc["description"],
                    noteCohereneEntreprise = int(cdc["description"]),
                    justificationNote = cdc["justificationNote"],
                    tempsProjet = cdc["tempsProjet"],
                    #prixGlobal = AI_SPIRIT
                    #prixGlobaleConcurrents = AI_SPIRIT
                )
                creaCDC.save()
                entreprise.nombreCDC += 1
                entreprise.save()
                
                ListeTaches = respPyJSON["project"][cdc]["taches"]
                for tache in ListeTaches:
                    if personality == 'AI_OPPORTUNITY':
                        creaTache = Tache.objects.create(
                            CahierDeCharge = cdc,
                            poste = tache["poste"],
                            descriptionTache = tache["description"],
                            tempsTache = tache["tempsTache"]
                        )
                    elif personality == 'AI_PERSEVERANCE':
                        creaTache = Tache.objects.create(
                            CahierDeCharge = cdc,
                            poste = tache["poste"],
                            descriptionTache = tache["description"],
                            tempsTache = tache["tempsTache"]
                            #prixTache =
                            #prixTacheConcurrents =
                        )
                        
                    cdc.tache.add(creaTache)
        
            # Appelle SPIRIT personality
            
            
                
            # Envoie dans le thread les taches 
            
                
                
            
        return HttpResponse(responseJSON)
            
        
        #La fin
        
        """
        patternDatabaseSpirit = r"<pricing>(.*?)</pricing>"  
        match = re.search(patternDatabase, htmlPropre, re.DOTALL)
        if match:
            personality='AI_SPIRIT'
            # Prends les taches et les prices et ensuite les sommes pour un globale
        """
            
    return render(request, 'discover/rovers.html')