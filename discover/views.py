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
    return render(request, 'discover/entreprises.html')

def projects(request):    
    return render(request,'discover/choixProjet.html')

def rovers(request):
    thread = create_thread()
    request.session['thread_id'] = thread.id
    return render(request, 'discover/rovers.html')

def freelances(request):
    return render(request, 'discover/freelances.html')

def histoire(request):
    return render(request, 'discover/histoire.html')


def roversPersonality(request):
    
    referring_url = request.META.get('HTTP_REFERER', 'Unknown')
    
    user = request.user
    entreprise = Entreprise.objects.get(user=user)
    
    personality = ''
    
    if entreprise.curiosityPass == False:
        personality = 'AI_CURIOSITY'
    elif 'projects' in referring_url and entreprise.curiosityPass:
        personality = 'AI_PERSEVERANCE'
    elif 'visions' in referring_url and entreprise.curiosityPass:
        personality = 'AI_OPPORTUNITY'
    else :
        print("erreur")
    
    
    thread_id = request.session.get('thread_id', None)
    ASSISTANT_ID = os.environ.get(personality)
    print(personality)
    print(ASSISTANT_ID)
    
    if request.method == "POST":
        message = request.POST.get('message')
        
        print(message)
        
        assistant = retrieve_assistant(ASSISTANT_ID)
        Add_message(message=message, thread_id=thread_id)
        
        responseHTML = run_assistant(assistant=assistant, thread_id=thread_id)
     
        htmlPropre = responseHTML
        if responseHTML[0:7] == "```html":
            htmlPropre = responseHTML[7:-3]
        
        print(htmlPropre)
        
        if personality == 'AI_CURIOSITY':
            patternDatabase = r"<database>(.*?)</database>"
            match = re.search(patternDatabase, htmlPropre, re.DOTALL)
            if match:
                resumeBusiness = match.group(1)
                entreprise.companyInformation = resumeBusiness
                entreprise.curiosityPass = True
                entreprise.save()
                return render(request, 'discover/rovers.html')
        elif personality == 'AI_OPPORTUNITY':
            pass
            # Validation du webData Pass
            # Ajout du réumer a la suite de company_information
            # Ajout de note et de prix sans détails
        elif personality == 'AI_PERSEVERANCE':
            # redaction cahier des charges dans description
            creaCahier = CahierDesCharges(
                user = entreprise,
                titre = '',
                description = ''
            )
            creaCahier.save()
            entreprise.nombreCDC += 1
            entreprise.save()
    
    return render(request, 'discover/rovers.html')