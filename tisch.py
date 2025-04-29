class Tisch:


    def __init__(self):  # Konstruktor für die Tischdaten
        self.aktuelle_wette = 0 # Aktuelle Wette (der höchste gesetzte Betrag), anfangs bei null
        self.ziehstapel = [] # Der Kartenvorrat (Deck), anfangs eine leere Liste
        self.community_cards = [] # Gemeinschaftskarten (Flop, Turn, River), anfangs eine leere Liste
        self.rundenanzahl = 1 # Anzahl der Runden, die gespielt werden sollen, wird anfangs auf 1 gesetzt, da in einem Spiel mindestens eine Runde gespielt wird, kann aber später noch angepasst werden bei der Tischerstellung
        self.spieler = [] # Liste der Spieler, anfangs leer
        self.pot = 0 # Pot (Gesamtbetrag der Einsätze), anfangs bei null
        self.raise_count = 0 # Zähler für die Anzahl der Erhöhungen in der Runde, anfangs bei null
        self.max_raises = 2  # Maximale Anzahl von Raises pro Runde, standardmäßig nach Pokerregeln bei 2
        self.spieleranzahl = int(input("Spieleranzahl: "))  # Eingabe der Anzahl der Spieler
        self.rundenanzahl = int(input("Rundenanzahl: "))  # Eingabe der Anzahl der Runden
        self.small_blind = int(input("Small Blind: "))  # Small Blind (Mindestwette)
        self.big_blind = 2 * self.small_blind   # Big Blind (doppelt so hoch wie Small Blind)

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