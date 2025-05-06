class Karte:
    def __init__(self,farbe:str,wert:int):
        self.farbe = farbe     # String
        self.wert = wert       # String (damit bube könig und dame erkennbar sind)
    

    def get_farbe(self):
        return self.farbe
    
    def get_wert(self):
        return self.wert
    
    def print_wert(self):
        #TODO zieht sich den String 11 -> Bube
        pass

    def print_karte(self):
        print("Die Karte ist " + self.farbe + " " + self.wert)