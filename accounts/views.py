from django.shortcuts import render
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.shortcuts import redirect

User = get_user_model()

def inscriptionFreelances(request):
    if request.method == "POST":
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        role = 'freelance'
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password == password2:
            user = User.objects.create_user(email=email, first_name=first_name, last_name=last_name, role=role, password=password)
            return render(request, 'accounts/connexion.html')
        else:
            return render(request, 'accounts/inscriptionFreelances.html', {'error': 'Les mots de passe ne correspondent pas'})
    return render(request, 'accounts/inscriptionFreelances.html')
        

def inscriptionEntreprises(request):
    if request.method == "POST":
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        role = 'entreprise'
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password == password2:
            user = User.objects.create_user(email=email, first_name=first_name, last_name=last_name, role=role, password=password)
            return render(request, 'accounts/connexion.html')
        else:
            return render(request, 'accounts/inscriptionEntreprises.html', {'error': 'Les mots de passe ne correspondent pas'})
    return render(request, 'accounts/inscriptionEntreprises.html')
        
        
def connexion(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(email=email, password=password)
        if user :
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'accounts/qui.html')
    return render(request, 'accounts/connexion.html')

                    
def qui(request):
    return render(request, 'accounts/qui.html')