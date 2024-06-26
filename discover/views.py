from django.shortcuts import render
from .AssistantAI.Assistant import *
from django.http import HttpResponse
from accounts.models import Entreprise
from discover.models import CahierDesCharges
import os
import re


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
    if entreprise.curiosityPass == False:
        personality = 'AI_CURIOSITY'
    if 'projects' in path_url and entreprise.curiosityPass:
        personality = 'AI_PERSEVERANCE'
    if 'visions' in path_url and entreprise.curiosityPass:
        personality = 'AI_OPPORTUNITY'
    
    
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
        responseHTML = run_assistant(assistant=assistant, thread_id=thread_id)
        htmlPropre = responseHTML
        if responseHTML[0:7] == "```html":
            htmlPropre = responseHTML[7:-3]
        print(htmlPropre)
        
        
        # Fin de conversation vers BDD   
        if personality == 'AI_CURIOSITY':
            patternDatabase = r"<database>(.*?)</database>"
            match = re.search(patternDatabase, htmlPropre, re.DOTALL)
            if match:
                resumeBusiness = match.group(1)
                entreprise.companyInformation = resumeBusiness
                entreprise.curiosityPass = True
                entreprise.save()
                return HttpResponse("finCuriosity")
            return HttpResponse(htmlPropre)
        
        elif personality == 'AI_OPPORTUNITY':
                patternDatabase = r"<database>(.*?)</database>"
                match = re.search(patternDatabase, htmlPropre, re.DOTALL)
                if match:
                    # Enregistrer dans la BDD (nouvelle table) les infos notes par projets pour l'entreprise -> réception sous forme de table
                    pass
                    # On ajoute AI_SPIRIT dans la continuiter, on lui donne directement le résumer, elle travaille et ensuite l'utilisateur peut revler le gain
                    personality = 'AI_SPIRIT'
                    
        elif personality == 'AI_PERSEVERANCE':
            # redaction cahier des charges dans description avec une spération des taches pour faciliter l'arriver de spirit
            creaCahier = CahierDesCharges(
                user = entreprise,
                titre = '',
                description = ''
            )
            creaCahier.save()
            entreprise.nombreCDC += 1
            entreprise.save()
            personality = 'AI_SPIRIT'
            
            
        
            
    return render(request, 'discover/rovers.html')