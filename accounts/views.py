from django.shortcuts import render
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.shortcuts import redirect
from django.db import transaction
from .forms import *


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
    return render(request, 'accounts/connexion.html')

def qui(request):
    return render(request, 'accounts/qui.html')