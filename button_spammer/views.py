from django.shortcuts import render
from django.http import HttpResponse
from .models import Action, Occurence

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the button-spammer index.")

def register(request, action_name):
    action = Action.objects.filter(action_name=action_name)
    if not action:
        return HttpResponse ("The action " + action_name + " does not exist. Can not create occurence.")

    occ = Occurence (action_name=action.get())
    occ.save()
    return HttpResponse("Occurence for action " + action_name + " registered.")
