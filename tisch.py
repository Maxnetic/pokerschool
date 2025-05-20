from spieler import *
import random
import os

class Tisch:
    def __init__(self):                                     # Konstruktor für die Tischdaten
        self.aktuelleWette = 0                             # Aktuelle Wette (der höchste gesetzte Betrag), anfangs bei null
        self.deck = []                                      # Der Kartenvorrat (Deck), anfangs eine leere Liste
        self.gemeinschaftskarten = []                       # Gemeinschaftskarten (Flop, Turn, River), anfangs eine leere Liste
        self.rundenanzahl = 1                               # Anzahl der Runden, die gespielt werden sollen, wird anfangs auf 1 gesetzt, da in einem Spiel mindestens eine Runde gespielt wird, kann aber später noch angepasst werden bei der Tischerstellung
        self.spielerListe = []                                   # Liste der Spieler, anfangs leer
        self.pot = 0                                        # Pot (Gesamtbetrag der Einsätze), anfangs bei null
        self.raiseCount = 0                                # Zähler für die Anzahl der Erhöhungen in der Runde, anfangs bei null
        #TODO: verschieben zu Validierung Raise() self.max_raises = 2                                 # Maximale Anzahl von Raises pro Runde, standardmäßig nach Pokerregeln bei 2
        self.rundenanzahl = int(input("Rundenanzahl: "))    # Eingabe der Anzahl der Runden
        self.smallBlind = int(input("Small Blind: "))      # Small Blind (Mindestwette)
        self.bigBlind = 2 * self.smallBlind               # Big Blind (doppelt so hoch wie Small Blind)

    def spielererstellung(self):                                #erstellt eine bestimmte Anzahl an Spielern mit Namen und Startvermoegen
        for i in range(int(input('Spieleranzahl:'))):
            teilnehmer = Spieler(name = input('Name: '), vermoegen = int(input('Startvermögen: ')))
            self.spielerListe.append(teilnehmer)

    def DeckErstellen(self):
        deck = []
        #erste Schleife teilt Farben zu, die zweite den Wert 
        for f in ["pik","herz","karo","kreuz"]:
            for w in [2,3,4,5,6,7,8,9,10,11,12,13,14]:
                deck.append(Karte(f,w))
        return(deck)
  
    def DeckMischen(self, deck):
        neuesDeck = []
        for i in range(52):
            pos = random.randint(0, len(deck) - 1)
            neuesDeck.append(deck[pos])
            deck.pop(pos)
        return neuesDeck

    def FlopAufdecken(self):
        self.gemeinschaftskarten = [self.deck.pop() for _ in range(3)]          # Ziehe 3 Karten für den Flop
        print(f"Flop: {[str(karte) for karte in self.gemeinschaftskarten]}")    # Zeige die Flop-Karten
    
    def TurnAufdecken(self):
        self.gemeinschaftskarten.append(self.deck.pop())                        # Ziehe eine Karte für den Turn
        print(f"Turn: {[str(karte) for karte in self.gemeinschaftskarten]}")    # Zeige die Turn-Karte

    def RiverAufdecken(self):
        self.gemeinschaftskarten.append(self.deck.pop())                        # Ziehe eine Karte für den River
        print(f"River: {[str(karte) for karte in self.gemeinschaftskarten]}")   # Zeige die River-Karte

    def konsole(self, communityCards, vermoegen, kartenhand):                  #spieler ui während einer runde
        print("aufgedeckte Karten: " + communityCards)                         #ausgeben der zum zeitpunkt wichtigen daten
        print("Hand: " + kartenhand)
        print("Vermögen: " + vermoegen)

        raise_call = ""
        while raiseCall is not in ["raise", "call"]:                           #input error handling
            raiseCall = input()

        if (raiseCall == "raise"):                             
              
            raiseMenge = 0
            while 0 < raiseMenge < Spieler.vermoegen:                      #input error handling
                raiseAmount = input("wie viel?: ")
                    
            Spieler.vermoegen = Spieler.vermoegen - raiseMenge         #vermoegen aktualisieren
            self.pot = self.pot + raiseMenge                           #pot aktualisieren

        elif (raiseCall == "call"):
            Spieler.aktiv = False                                           #spieler scheiden aus bei call

        os.system('cls' if os.name == 'nt' else 'clear')
        
    def zeigeSpielstaende(self):                                               #ausgeben von name und vermoegen aller spieler
        for i in spieler:
            print(i.name + " " + i.vermoegen)                       

