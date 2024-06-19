from django.shortcuts import render
from .AssistantAI.Assistant import *
from django.http import HttpResponse
import os


def index(request):
    return render(request, 'discover/index.html')

def entreprises(request):
    thread = create_thread()
    request.session['thread_id'] = thread.id
    return render(request, 'discover/entreprises.html')

def freelances(request):
    return render(request, 'discover/freelances.html')

def histoire(request):
    return render(request, 'discover/histoire.html')


def BotCreationProjet(request):
    
    thread_id = request.session.get('thread_id', None)
    ASSISTANT_ID = os.environ.get('OPENAI_ASS_CDC_KEY')
    
    if request.method == "POST":
        message = request.POST.get('message')
        
        print(message)
        
        assistant = retrieve_assistant(ASSISTANT_ID)
        Add_message(message=message, thread_id=thread_id)
        
        responseHTML = run_assistant(assistant=assistant, thread_id=thread_id)
        print(responseHTML)
        
        return HttpResponse(responseHTML)
    
    return render(request, 'discover/entreprises.html')