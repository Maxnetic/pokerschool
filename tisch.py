import spieler

class Tisch:

    def __init__(self):
        self.sb = input('Betrag des Small Blinds (sb):')
        self.spielerliste = []
        self.startvermögen = int(input('Startvermögen:'))
        spieleranzahl = int(input('Spieleranzahl:'))
    
    def spielererstellung(self):
        for i in range(spieleranzahl):
            self.spielerliste.append(spieler = spieler(vermoegen = int(input('Startvermögen: '), name = input('name. '))))

    def deck_erstellen(self):
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



a = Tisch()
a.spielererstellung()