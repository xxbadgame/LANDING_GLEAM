from openai import OpenAI
import time
import os

client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
if not client:
    raise ValueError("The AI_API_KEY environment variable is not set.")

def create_assistant():
    assistant = client.beta.assistants.create(
        name="AssistantAI",
        description="Speak with human",
        model="gpt-3.5-turbo",
    )
    return assistant

def retrieve_assistant(id_assistant):
    assistant = client.beta.assistants.retrieve(id_assistant)
    return assistant

def create_thread():
    thread = client.beta.threads.create()
    return thread

def Add_message(message, thread_id):
    message = client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=message
    )
    
def run_assistant(assistant, thread_id):
    
    run = client.beta.threads.runs.create(
        thread_id = thread_id,
        assistant_id = assistant.id,
    )
    
    while run.status != 'completed': 
        run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)
        print(run.status)
    else:
        print("finish")
    
    messages = client.beta.threads.messages.list(thread_id=thread_id)
    
    messages_data = messages.data[0]
    
    latest_message = messages_data.content[0].text.value
    
    return latest_message
    
    