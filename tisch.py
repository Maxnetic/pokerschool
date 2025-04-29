class Tisch:

    def __init__(self, spieleranzahl, smallBlind):
        self.spieleranzahl = spieleranzahl
        self.smallBlind = smallBlind

    def Spielererstellung(self):
        pass

    def Deck_erstellen(self):
        kartenDeck = []
        #erste Schleife teilt Farben zu, die zweite den Wert 
        for f in range(4):
            for w in range(2, 15):
                if(f==1):
                    f = "pik"
                if(f==2):
                    f = "herz"
                if(f==3):
                    f = "kreuz"
                if(f==0):
                    f = "karo"
                if(w==11):
                    w = "bube"
                if(w==12):
                    w = "dame"
                if(w==13):
                    w = "koenig"
                if(w==14):
                    w = "ass"
                #dann werden die Kartenobjekte erstellt und in eine Liste sortiert
                #name = w, damit die objekte in die Liste sortiert werden und nicht die Variable w
                name = w
                name = Karte(f, w)
                kartenDeck.append(name)
        return kartenDeck
           
    def turn(self):
        aufgedeckeKarten.append(kartenDeck[0])
        return aufgedeckteKarten