"""
skill skryfall
"""

from mycroft import MycroftSkill, intent_file_handler
from mycroft.util.parse import match_one
from mycroft.audio import wait_while_speaking
import requests
import time

import scrython

class SkryfallSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.is_reading = False

    @intent_file_handler('readFlavourText.intent')
    def handle_fairytalez(self, message):
        if message.data.get("cardName") is None:
            response = self.get_response('skryfall', num_retries=0)
            if response is None:
                return
        else:
            response = message.data.get("cardName")
        self.speak_dialog('let_me_think', data={"cardName": response})

        card = scrython.cards.Named(fuzzy=response)

        self.speak_dialog('flavourtext',data={"cardName": response, "flavor_text": card.flavor_text()})



def create_skill():
    return SkryfallSkill()
