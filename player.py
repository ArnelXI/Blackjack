class Player:
    hand=[]
    solde = 1000
    def __init__(self,username,password,firstname,lastname):
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
    
    def active_game(self,data):
        if(data):
            return True
        else:
            return False
    
    # def handle_hand(self):
    #     #check if the player is in any active game then allow him to get cards
    #     if active_game:
            
    
    def bet(self,montant):
        self.solde = self.solde - montant