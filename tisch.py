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