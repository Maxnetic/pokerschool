class Karte:
    def __init__(self,farbe,wert):
        self.farbe = farbe     # String
        self.wert = wert       # String (damit bube könig und dame erkennbar sind)
    

    def getFarbe(self):
        return self.farbe
    
    def getWert(self):
        return self.wert

    def printKarte(self):
        print("Die Karte ist " + self.farbe + " " + self.wert)

    


class Tisch:

    def __init__(self):
        self.startvermögen = input('Startvermögen:')
        self.spieleranzahl = input('Spieleranzahl:')
        self.sb = input('Betrag des Small Blinds (sb):')

    def Spielererstellung(self):
        pass

    def Deck_erstellen(self):
        kartenDeck = [] 
        for i in range(2,15):  
             
            if(j == 11):
                for j in range(13):    # alle werte der Farbe
            if(j == 11):
                wert = "Bube"
            elif j == 12:
                wert = "Dame"
            elif j == 13:
                wert = "König"
            elif j == 14:
                wert = "Ass"
            else:
                wert = j







class Spieler:
    def __init__(self, vermoegen, name, aktiv = True, kartenhand = 0):
        #der Spieler wird erstellt
        self.name = name
        self.kartenhand = kartenhand
        self.aktiv = aktiv
        self.vermoegen = vermoegen

    def Call(self, betrag):
        #hier muss der betrag dem Tisch zuaddiert werden
        #tisch.add_pot(betrag)
        #das Vermögen wird gesengt
        self.vermoegen = self.vermoegen - betrag
        return self.vermoegen

    def Fold(self):
        #hier muss der Spieler aus der Liste der Beteiligten gelöscht werden
        #Der Status wird auf raus gesetzt
        self.aktiv = False
        return self.aktiv

    def Raise(self, betrag):
        #hier muss der Betrag dem Tisch zugeordnet werden
        #tisch.add_pot(betrag)
        #der Betrag wird dem vermögen abgezogen
        self.vermoegen = vermoegen - betrag

    def get_Hand(self): #Gibt die aktuelle Hand aus
        print('Hand: ' + self.kartenhand)

    def All_In(self, betrag):
        betrag = self.vermoegen
        self.vermoegen = 0
        return betrag

    def kartenausteilen(self, karten):
        #der Tisch greift auf dise Methode beim Kartenausteilen zu
        self.kartenhand = karten
        return self.kartenhand