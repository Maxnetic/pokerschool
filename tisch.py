from spieler import *

class Tisch:

    def __init__(self):
        self.sb = input('Betrag des Small Blinds (sb):')        #fragt nach Größe des small Blinds und erstellt eine leere Spielerliste
        self.spielerliste = []
    
    def spielererstellung(self):                                #erstellt eine bestimmte Anzahl an Spielern mit Namen und Startvermoegen
        for i in range(int(input('Spieleranzahl:'))):
            teilnehmer = Spieler(name = input('Name: '), vermoegen = int(input('Startvermögen: ')))
            self.spielerliste.append(teilnehmer)

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

