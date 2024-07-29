from django.shortcuts import render
from .AssistantAI.Assistant import *
from django.http import HttpResponse
from accounts.models import Entreprise
from discover.models import CahierDeCharge, Tache
import os
import json


def index(request):
    return render(request, 'discover/index.html')

def freelanceIa(request):
    return render(request, 'discover/ia-freelances.html')

def rovers(request):
    thread = create_thread()
    request.session['thread_id'] = thread.id
    
    projet = request.POST.get('projet')
    request.session['projet_name'] = projet
    
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


def roversPersonality(request):
    
    # Récuperer les infos users et entreprise en BDD
    user = request.user
    entreprise = Entreprise.objects.get(user=user)

    personality = 'AI_CURIOSITY'
    
    # execution thread et de l'assistant
    thread_id = request.session.get('thread_id', None)
    ASSISTANT_ID = os.environ.get(personality)
    assistant = retrieve_assistant(ASSISTANT_ID)
    
    # Réception message, traitement et renvoie au front
    if request.method == "POST":
        
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
                        
            
        return HttpResponse(responseJSON)
        
    return render(request, 'discover/rovers.html')
