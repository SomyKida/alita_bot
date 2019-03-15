# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import json
from rasa_core_sdk import Action


logger = logging.getLogger(__name__)


class ActionJoke(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_joke"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        request = json.loads(requests.get('https://api.chucknorris.io/jokes/random').text)  # make an api call
        joke = request['value']  # extract a joke from returned json response
        dispatcher.utter_message(joke)  # send the message back to the user
        return []

class Action_Get_Hours(Action):
    def name(self):
        return "action_get_hours"
    
    def run(self, dispatcher, tracker, domain):
        print(tracker.latest_message)
        dispatcher.utter_message(tracker.get_slot('email'))
        try:
            email = tracker.get_slot('email')

            r = requests.get("http://localhost:5000/api/dentist/dashboard/get-slots?email=enigcreator@gmail.com", headers={'content-type' : 'application/json'})
            json_data = json.loads(r.text)
            print(json_data)
            dispatcher.utter_message(json_data['data'])

        except():
            dispatcher.utter_message(tracker.get_slot('email'))
        
        dispatcher.utter_message(tracker.get_slot('email'))
        return []