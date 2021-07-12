from Class import class
import Card
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
            