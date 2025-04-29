class Tisch:


# Klasse Tisch Methode: Spielererstellung (soll die Spieler-, Rundenanzahl,
#  das Startvermögen, den Small Blind und den Big Blind implementieren sowie reihum die Spieler ihren Namen eingeben lassen)
    def __init__(self):
        self.aktuelle_wette = 0
        self.ziehstapel = []
        self.community_cards = []
        self.rundenanzahl = 1
        self.spieler = []
        self.pot = 0
        self.raise_count = 0
        self.max_raises = 2

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