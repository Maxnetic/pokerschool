from spieler import *
import random
import os

class Tisch:
    def __init__(self):                                     # Konstruktor für die Tischdaten
        self.aktuelle_wette = 0                             # Aktuelle Wette (der höchste gesetzte Betrag), anfangs bei null
        self.deck = []                                      # Der Kartenvorrat (Deck), anfangs eine leere Liste
        self.gemeinschaftskarten = []                       # Gemeinschaftskarten (Flop, Turn, River), anfangs eine leere Liste
        self.rundenanzahl = 1                               # Anzahl der Runden, die gespielt werden sollen, wird anfangs auf 1 gesetzt, da in einem Spiel mindestens eine Runde gespielt wird, kann aber später noch angepasst werden bei der Tischerstellung
        self.spielerListe = []                                   # Liste der Spieler, anfangs leer
        self.pot = 0                                        # Pot (Gesamtbetrag der Einsätze), anfangs bei null
        self.raise_count = 0                                # Zähler für die Anzahl der Erhöhungen in der Runde, anfangs bei null
        #TODO: verschieben zu Validierung Raise() self.max_raises = 2                                 # Maximale Anzahl von Raises pro Runde, standardmäßig nach Pokerregeln bei 2
        self.rundenanzahl = int(input("Rundenanzahl: "))    # Eingabe der Anzahl der Runden
        self.small_blind = int(input("Small Blind: "))      # Small Blind (Mindestwette)
        self.big_blind = 2 * self.small_blind               # Big Blind (doppelt so hoch wie Small Blind)

    def spielererstellung(self):                                #erstellt eine bestimmte Anzahl an Spielern mit Namen und Startvermoegen
        for i in range(int(input('Spieleranzahl:'))):
            teilnehmer = Spieler(name = input('Name: '), vermoegen = int(input('Startvermögen: ')))
            self.spielerListe.append(teilnehmer)

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

    def Flop_aufdecken(self):
        self.gemeinschaftskarten = [self.deck.pop() for _ in range(3)]          # Ziehe 3 Karten für den Flop
        print(f"Flop: {[str(karte) for karte in self.gemeinschaftskarten]}")    # Zeige die Flop-Karten
    
    def Turn_aufdecken(self):
        self.gemeinschaftskarten.append(self.deck.pop())                        # Ziehe eine Karte für den Turn
        print(f"Turn: {[str(karte) for karte in self.gemeinschaftskarten]}")    # Zeige die Turn-Karte

    def River_aufdecken(self):
        self.gemeinschaftskarten.append(self.deck.pop())                        # Ziehe eine Karte für den River
        print(f"River: {[str(karte) for karte in self.gemeinschaftskarten]}")   # Zeige die River-Karte

    def konsole(self, spieler, community_cards, vermoegen, kartenhand):                  #spieler ui während einer runde
        print("aufgedeckte Karten: " + community_cards)                         #ausgeben der zum zeitpunkt wichtigen daten
        print("Hand: " + kartenhand)
        print("Vermögen: " + vermoegen)

        raise_call_fold = ""
        betrag = ""                           #input error handling

        if raise_call_fold == "Raise":
            betrag = input()                             
            spieler.Raise(betrag)                          #pot aktualisieren
        elif raise_call_fold == "Call":
            betrag = input()
            spieler.Call(betrag)
        elif raise_call_fold == "Fold":
            spieler.Fold()        
        else:
            raise_call_fold = input("Raise Call oder Fold?:")                    
                                             #spieler scheiden aus bei call
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def zeige_spielstaende(self):                                               #ausgeben von name und vermoegen aller spieler
        for spieler in self.spielerListe:
            print(spieler.name + " " + spieler.vermoegen)   
