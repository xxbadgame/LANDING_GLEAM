from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.db import transaction
from .forms import *
from discover.models import CahierDeCharge


def inscriptionFreelances(request):
    if request.method == 'POST':
        user_form = CustomUserForm(request.POST)
        freelance_form = FreelanceForm(request.POST)
        if user_form.is_valid() and freelance_form.is_valid() :
            with transaction.atomic():
                user = user_form.save(commit=False)
                user.role = 'freelance'
                user.save()
                freelance = freelance_form.save(commit=False)
                freelance.user = user
                freelance.save()
            return redirect('index')
    else:
        user_form = CustomUserForm()
        freelance_form = FreelanceForm()
    return render(request,'accounts/inscriptionFreelances.html', {'user_form':user_form ,'freelance_form':freelance_form})

def inscriptionEntreprises(request):
    if request.method == 'POST':
        user_form = CustomUserForm(request.POST)
        entreprise_form = EntrepriseForm(request.POST)
        if user_form.is_valid() and entreprise_form.is_valid() :
            with transaction.atomic():
                user = user_form.save(commit=False)
                user.role = 'entreprise'
                user.save()
                entreprise = entreprise_form.save(commit=False)
                entreprise.user = user
                entreprise.save()
            return redirect('index')
    else:
        user_form = CustomUserForm()
        entreprise_form = EntrepriseForm()
    return render(request,'accounts/inscriptionEntreprises.html', {'user_form':user_form ,'entreprise_form': entreprise_form})


def connexion(request):
    if request.method == 'POST':
        form = ConnexionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, "Identifiants invalides")
    else:
        form = ConnexionForm()
    
    return render(request, 'accounts/connexion.html', {'form' : form})

def deconnexion(request):
    logout(request)
    return redirect('index')

def qui(request):
    return render(request, 'accounts/qui.html')

def profil(request):
    
    context = {}
    user = request.user
    if user.role == "entreprise":
        entreprise = Entreprise.objects.get(user=user)
        cahiers_des_charges = CahierDeCharge.objects.filter(user=entreprise,discover=False).prefetch_related('taches')
        context = {
            'cahiers_des_charges': cahiers_des_charges,
        }
    
    return render(request, 'accounts/profil.html', context)