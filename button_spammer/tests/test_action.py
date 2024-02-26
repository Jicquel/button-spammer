from django.test import TestCase
from django.urls import reverse, resolve
from button_spammer.models import Action
from button_spammer.views import create_action


class ActionTest(TestCase):
    def setUp(self):
        Action.objects.create(action_name="action_1")
        Action.objects.create(action_name="action_2")

    def test_creation(self):
        """Action creation"""
        a1 = Action.objects.get(action_name="action_1")
        a2 = Action.objects.get(action_name="action_2")
        self.assertEqual(a1.action_name, "action_1")
        self.assertEqual(a2.action_name, "action_2")

    def test_url_creation(
        self,
    ):
        name = "action_3"
        path = reverse("create_action")
        response = self.client.post(path, data={"name": name})
        action = Action.objects.get(action_name=name)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(action.action_name, name)

        path = reverse("delete_action", args=[name])
        response = self.client.post(path, data={"name": name})
        self.assertFalse(Action.objects.filter(action_name=name).exists())
