#!/bin/env python3
import requests

# x = requests.get('http://127.0.0.1:8000/button-spammer/actions/json')
# print(x.status_code)
# actions = x.json()["actions"]
# print(actions)


class Actions:

    selected_action_idx = 0
    actions = []

    def __init__(self):
        resp = requests.get('http://127.0.0.1:8000/button-spammer/actions/json')
        if (resp.status_code == 200):
            self.actions = [a["name"] for a in resp.json()["actions"]]
            self.selected_action_idx = 0

    def current_action(self):
        return self.actions[self.selected_action_idx]

    def next_action(self):
        self.selected_action_idx = (self.selected_action_idx + 1) % len (self.actions)
        return self.current_action


actions = Actions()
print(actions.current_action())
print(actions.next_action())

