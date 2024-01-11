from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

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

def create_action_form(request):
    template = loader.get_template("action_creation.html")
    return HttpResponse(template.render({}, request))

def create_action(request):
    action_name = request.POST["name"]
    action = Action.objects.filter(action_name=action_name)

    if action:
        return HttpResponse("Action " + action_name + " already exist.")

    action = Action (action_name = action_name)
    action.save()
    return HttpResponse("Action " + action_name + " has been created.")
