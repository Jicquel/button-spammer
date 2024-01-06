from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the button-spammer index.")

def register(request, action_id):
    return HttpResponse("Hello, you tried to register the action n. " + str(action_id))
