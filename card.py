class Card:
    def __init__(self,img_face,img_dos,numerik_value):
        self.img_face = img_face
        self.img_dos = img_dos
        self.numerik_value = numerik_value

    def getImgFace(self):
        return self.img_face
    
    def getImgDos(self):
        return self.img_dos
    
    def getNumerikValue(self):
        return self.numerik_value