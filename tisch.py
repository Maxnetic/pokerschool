class Tisch:

    def __init__(self):
        self.sb = input('Betrag des Small Blinds (sb):')

    def Spielererstellung(self):
        self.startvermögen = input('Startvermögen:')
        self.spieleranzahl = input('Spieleranzahl:')
        for i in range(self.spieleranzahl):
            i.spieler = Spieler(vermoegen = self.startvermögen, name = input("name?"))

    def Deck_erstellen(self):
        kartenDeck = [] 
        for i in range(2,15):  
             
            if(j == 11):
                for j in range(13):
                    pass()    # alle werte der Farbe
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