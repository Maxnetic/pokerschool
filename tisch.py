import random

class Tisch:
    def __init__(self):                                     # Konstruktor für die Tischdaten
        self.aktuelle_wette = 0                             # Aktuelle Wette (der höchste gesetzte Betrag), anfangs bei null
        self.deck = []                                      # Der Kartenvorrat (Deck), anfangs eine leere Liste
        self.gemeinschaftskarten = []                       # Gemeinschaftskarten (Flop, Turn, River), anfangs eine leere Liste
        self.rundenanzahl = 1                               # Anzahl der Runden, die gespielt werden sollen, wird anfangs auf 1 gesetzt, da in einem Spiel mindestens eine Runde gespielt wird, kann aber später noch angepasst werden bei der Tischerstellung
        self.spieler = []                                   # Liste der Spieler, anfangs leer
        self.pot = 0                                        # Pot (Gesamtbetrag der Einsätze), anfangs bei null
        self.raise_count = 0                                # Zähler für die Anzahl der Erhöhungen in der Runde, anfangs bei null
        #TODO: verschieben zu Validierung Raise() self.max_raises = 2                                 # Maximale Anzahl von Raises pro Runde, standardmäßig nach Pokerregeln bei 2
        #TODO: verschieben zu Spielerstellung self.spieleranzahl = int(input("Spieleranzahl: "))  # Eingabe der Anzahl der Spieler
        self.rundenanzahl = int(input("Rundenanzahl: "))    # Eingabe der Anzahl der Runden
        self.small_blind = int(input("Small Blind: "))      # Small Blind (Mindestwette)
        self.big_blind = 2 * self.small_blind               # Big Blind (doppelt so hoch wie Small Blind)

    def Spielererstellung(self):
        #TODO
        pass

    def Deck_erstellen(self):
        deck = []
        #erste Schleife teilt Farben zu, die zweite den Wert 
        for f in ["pik","herz","karo","kreuz"]:
            for w in [2,3,4,5,6,7,8,9,10,11,12,13,14]:
                deck.append(Karte(f,w))
        return(deck)
  
    def Deck_mischen(self, deck):
        neues_deck = []
        for i in range(52):
            pos = random.randint(0, len(deck) - 1)
            neues_deck.append(deck[pos])
            deck.pop(pos)
        return neues_deck