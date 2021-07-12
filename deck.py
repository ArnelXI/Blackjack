import random
import card
from pathlib import Path

Class Deck:
    def __init__:
        deck = []
        img_back = Path('carte_back')
        img_front = Path('carte_front')
        numerik_value = 2
        #adding the card to the Deck
        for i in range(0,12):
            for i in range(0,3):
                deck.append(Card(img_back,img_front,numerik_value))
            numerik_value = numerik_value + 1
        for in range(0,3):
            deck.append(Card(img_back,img_front,"AS"))
    
    def serve(self):
        hand = []
        for i in range(0,1):
            hand.append(random.choice(self.deck))
        return hand
    
    def hit(self):
        return randonm.choice(self.deck)
    
    
            