from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_occurence/<str:action_name>/", views.create_occurence, name="create_occurence"),
    path("create_action/", views.create_action, name="create_action"),
    path("create_action_form/", views.create_action_form, name="create_action_form"),
    path("action/<str:action_name>/", views.action, name="action"),
    path("actions/", views.actions, name="actions"),
    path("delete_action/<str:action_name>/", views.delete_action, name="delete_action"),
]
