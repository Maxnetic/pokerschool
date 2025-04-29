class Karte:
    def __init__(self,farbe:str,wert:int):
        self.farbe = farbe     # String
        self.wert = wert       # String (damit bube könig und dame erkennbar sind)
    

    def getFarbe(self):
        return self.farbe
    
    def getWert(self):
        return self.wert
    
    def printWert(self):
        #TODO zieht sich den String 11 -> Bube
        pass

    def printKarte(self):
        print("Die Karte ist " + self.farbe + " " + self.wert)