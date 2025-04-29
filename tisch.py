class Tisch:

    def __init__(self):
        self.startvermögen = input('Startvermögen:')
        self.spieleranzahl = input('Spieleranzahl:')
        self.wette = input('Wette:')
        self.sb = input('Betrag des Small  (sb):')
        self.rundenAnzahl = input('Rundenanzahl:')
       

    def Spielererstellung(self):
        pass

    def Deck_erstellen(self):
        kartenDeck = [] 
        for i in range(2,15):  


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



    def kartenAusteilen(self):
        for i in range(len(spielerListe)):
            spieler = spielerListe[i]
            spieler.set_Hand()

