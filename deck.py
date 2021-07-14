import random
import card
from pathlib import Path

class Deck:
    def __init__(self):
        deck = []
        img_back = Path('carte_back')
        img_front = Path('carte_front')
        numerik_value = 2
        #adding the card to the Deck
        for i in range(0,12):
            for i in range(0,3):
                deck.append(card(img_back,img_front,numerik_value))
            numerik_value = numerik_value + 1
        for in range(0,3):
            deck.append(card(img_back,img_front,"AS"))
    
    def serve(self):
        hand = []
        for i in range(0,1):
            choice = random.choice(self.deck)
            hand.append(choice)
            self.deck.pop(choice)
        return hand
    
    def hit(self):
        choice = random.choice(self.deck)
        self.deck.pop(choice)
        return choice