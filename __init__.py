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

    @intent_file_handler('doYouKnowAboutMagic.intent')
    def handle_skryfall(self, message):
        response = self.get_response('skryfall')


    @intent_file_handler('readFlavourText.intent')
    def handle_flavorText(self, message):
        cardName = message.data.get("cardName")
        self.speak_dialog('let_me_think', data={"cardName": cardName})

        card = scrython.cards.Named(fuzzy=cardName)

        self.speak_dialog('flavourtext',data={"cardName": cardName, "flavor_text": card.flavor_text()})


def create_skill():
    return SkryfallSkill()
