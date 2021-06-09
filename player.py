class Player:
    def __init__(self,username,password,firstname,lastname):
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.solde = 1000
        self.hand = []
        self.hand_1 = []
    
    def handle_hand(self,card1,card2):
        self.hand.append(card1,card2)

    def bet(self,montant):
        self.solde = self.solde - montant

    def split(self):
        self.hand_1 = self.hand[0]
    
    def bet(self,montant):
        self.solde = self.solde-montant
        return montant
    
    
