from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader


from .models import Action, Occurence
from django.template import loader

# Create your views here.


def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render({}, request))


##############
# Occurences #
##############


def create_occurence(request, action_name):
    act = Action.objects.filter(action_name=action_name)
    if not act:
        return HttpResponse(
            "The action " + action_name + " does not exist. Can not create occurence."
        )

    occ = Occurence(action_name=act.get())
    occ.save()
    return action(request, action_name)


###########
# Actions #
###########


def create_action_form(request):
    template = loader.get_template("actions/create.html")
    return HttpResponse(template.render({}, request))


def create_action(request):
    action_name = request.POST["name"]
    action = Action.objects.filter(action_name=action_name)

    if action:
        return HttpResponse("Action " + action_name + " already exist.")

    action = Action(action_name=action_name)
    action.save()
    return HttpResponse("Action " + action_name + " has been created.")


def action(request, action_name):
    action = Action.objects.filter(action_name=action_name)

    if not action:
        return HttpResponse("The action " + action_name + " does not exist.")

    occurences = Occurence.objects.filter(action_name=action_name)

    template = loader.get_template("actions/action.html")
    context = {"action": action.first, "occurences_list": occurences}
    return HttpResponse(template.render(context, request))


def actions(request, format="web"):
    actions = Action.objects.all()

    template = loader.get_template("actions/actions.html")

    if format == "json":
        data = {}
        data["actions"] = [{"name": a.action_name} for a in actions]
        return JsonResponse(data)

    context = {
        "actions_list": actions,
    }
    return HttpResponse(template.render(context, request))


def delete_action(request, action_name):
    action = Action.objects.filter(action_name=action_name)

    if not action:
        return HttpResponse("The action " + action_name + " does not exist.")

    action.delete()
    return actions(request)
