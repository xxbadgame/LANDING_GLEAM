from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import redirect

class RoleCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if '/creation_mission/' in request.path:
            if not request.user.is_authenticated:
                return redirect('login')
            elif request.user.role != 'entreprise':
                return HttpResponseForbidden("Accès refusé : Vous devez être une entreprise connectée pour accéder à cette page.")

        return self.get_response(request)