from spieler import *
from karte import *
import random
import os

class Tisch:
    def __init__(self):                                     # Konstruktor für die Tischdaten
        self.aktuelleWette = 0                             # der höchste gesetzte Betrag
        self.gemeinschaftskarten = []                       # Gemeinschaftskarten sind die Karten für Flop, Turn, River
        self.ablagestapel = []
        self.spielerListe = []                              # Mitspielende Spieler
        self.pot = 0                                        # Gesamtbetrag der Einsätze
        self.raiseCount = 0                                # Zähler für die Anzahl der Erhöhungen in der Runde                         
        self.rundenanzahl = int(input("Rundenanzahl: "))    # Eingabe der Anzahl der Runden
        self.smallBlind = int(input("Small Blind: "))      # Small Blind (Mindestwette)
        self.bigBlind = int(input("Big Blind: "))           # Error handling todo!
        #self.blindincreaseafterrounds...

    def spielererstellung(self):                                #erstellt eine bestimmte Anzahl an Spielern mit Namen und Startvermoegen
        for i in range(int(input('Spieleranzahl:'))):
            teilnehmer = Spieler(name = input('Name: '), vermoegen = int(input('Startvermögen: '), tisch = self))
            self.spielerListe.append(teilnehmer)

    def deckErstellen(self):
        deck = []
        #erste Schleife teilt Farben zu, die zweite den Wert 
        for farbe in ["pik","herz","karo","kreuz"]:
            for wert in [2,3,4,5,6,7,8,9,10,11,12,13,14]:
                deck.append(Karte(farbe, wert))
        return(deck)
    
    def deckAusgeben(self, deck):
        for Karte in deck:
            print(Karte.printWert())
  
    def deckMischen(self, deck): # Deck wird in neuesDeck umbenannt
        neuesDeck = []
        for i in range(52):
            pos = random.randint(0, len(deck) - 1)
            neuesDeck.append(deck[pos])
            deck.pop(pos)
        return neuesDeck
    
    def kartenAusteilen(spielerListe,deck):
        deckIndex = 0
        for spieler in spielerListe:
            spieler.setHand([deck[deckIndex],deck[deckIndex + 1]])
            deckIndex = deckIndex + 2

    def aktionVerarbeiten(aktion, spieler):
        match aktion:
            case "r":
                    betrag = spieler.Raise()
                    if(betrag > aktuelleWette):
                        aktuelleWette = betrag
                        setPot(betrag)
                        for spieler in spielerListe:
                            spieler.setFertig(False)
                    
                         
                    else:
                         print("Fehler")
                    return "r"

            case "c":
                    spieler.Call()
                    setPot(self.aktuelleWette)
                    spieler.setFertig(True)
                    return "c"
            case "f":
                    spieler.fold()
                    return "f"

            case "allIn":
                    betrag = spieler.allIn()
                    setPot(betrag)
                    return "allIn"
                    spieler.setFertig(True)

            case _:
                    print("Eingabe ist falsch")



    def alleFertig(spielerListe):
         fertig = False
         for spieler in spielerListe:
              fertig = spieler.getFertig()
         return fertig
         
    def flopAufdecken(self, neuesDeck):
        self.gemeinschaftskarten = [neuesDeck.pop() for _ in range(3)]          # Ziehe 3 Karten für den Flop
        print(f"Flop: {[str(karte) for karte in self.gemeinschaftskarten]}")    # Zeige die Flop-Karten
    
    def turnAufdecken(self, neuesDeck):
        self.gemeinschaftskarten.append(neuesDeck.pop())                        # Ziehe eine Karte für den Turn
        print(f"Turn: {[str(karte) for karte in self.gemeinschaftskarten]}")    # Zeige die Turn-Karte

    def riverAufdecken(self, neuesDeck):
        self.gemeinschaftskarten.append(neuesDeck.pop())                        # Ziehe eine Karte für den River
        print(f"River: {[str(karte) for karte in self.gemeinschaftskarten]}")   # Zeige die River-Karte
        
    def zeigeSpielstaende(self):                                               #ausgeben von name und vermoegen aller spieler
        for spieler in self.spielerListe:
            print(spieler.name + " " + spieler.vermoegen)   

    def getGemeinschaftskarten(self):
        return(self.gemeinschaftskarten)


    def getPot(self):
        #Aktualisierung erfolgt bei Abruf, ergibt sich aus aktuellen Wetten der Spieler
        self.pot = 0
        for spieler in self.spielerListe:
             self.pot = self.pot + spieler.aktuelleWette
        return self.pot

