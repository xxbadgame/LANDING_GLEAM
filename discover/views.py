from django.shortcuts import render
from .AssistantAI.Assistant import *
from django.http import HttpResponse
import os


def index(request):
    return render(request, 'discover/index.html')

def entreprises(request):
    return render(request, 'discover/entreprises.html')

def curiosity(request):
    thread = create_thread()
    request.session['thread_id'] = thread.id
    return render(request, 'discover/curiosity.html')

def freelances(request):
    return render(request, 'discover/freelances.html')

def histoire(request):
    return render(request, 'discover/histoire.html')


def BotCreationProjet(request):
    
    thread_id = request.session.get('thread_id', None)
    ASSISTANT_ID = os.environ.get('AI_CURIOSITY')
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
        return HttpResponse(htmlPropre)
    
    return render(request, 'discover/curiosity.html')