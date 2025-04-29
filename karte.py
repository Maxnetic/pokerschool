class Karte:
    def __init__(self,farbe,wert):
        self.farbe = farbe     # String
        self.wert = wert       # String (damit Bube, König und Dame erkennbar sind)
    

    def getFarbe(self):
        return self.farbe
    
    def getWert(self):
        return self.wert

    def printKarte(self):
        return f"{self.wert}{self.farbe}"
  