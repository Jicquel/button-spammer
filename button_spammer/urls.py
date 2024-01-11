from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/<str:action_name>/", views.register),
    path("create_action/", views.create_action, name="create_action"),
    path("create_action_form/", views.create_action_form, name="create_action_form")
]
