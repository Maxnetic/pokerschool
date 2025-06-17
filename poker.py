import spieler,tisch,karte
from tisch import *
from spieler import *
from karte import *

runde = 1
tisch = Tisch()
tisch.spielererstellung()
tisch.deckErstellen()
tisch.deckMischen()
for i in range (len(tisch.spielerListe)):
    tisch.spielerListe[i].kartenhand = [tisch.neuesDeck[0], tisch.neuesDeck[1]]
    tisch.neuesDeck.remove[0]
    tisch.neuesDeck.remove[0]

tisch.spielerListe[0].vermoegen = tisch.spielerListe[0].vermoegen - tisch.smallBlind
tisch.spielerListe[1].vermoegen = tisch.spielerListe[1].vermoegen - tisch.bigBlind

def printStatus(): 
    pass

def spielablauf(start):
    for k in range (start, start + len(tisch.spielerListe)):
        i = k % tisch.spielerListe
        naechsterSpieler = str(tisch.spielerListe[i])
        print("der nächste Spieler ist: " + naechsterSpieler)
        bereit = input("Gib etwas ein, wenn du bereit bist")
        printStatus(tisch.spielerListe[i])
        aktion = input("was ist deine naechste Aktion? Raise (r), Call (c), Fold (f) oder all in (allin)?")
        if aktion == 'r':
            hoehe = int(input("um wie viel?")) + tisch.aktuelleWette
            tisch.spielerListe[i].Raise(hoehe)
            tisch.pot = tisch.pot + hoehe
            spielablauf(i)
        if aktion == "c":
            tisch.spielerListe[i].call(tisch.aktuelleWette)
            tisch.pot = tisch.pot + tisch.aktuelleWette
        if aktion == "f":
            tisch.spielerListe[i].fold()



    


#tisch erstellen
#spieler erstellen
#karten erstellen und mischen
#karten an spieler austeilen

#liste von spielerobjekten, die in der position wechseln

#print in die Konsole mit aktuellem Spieler
#bereitschaft
#print aktuellen spielstatus: hand, eigenes geld, pot, aufgedeckte karten, verbliebene spieler usw.
#input aktion
# r -> wie viel?, auch bei anderen spielern da?
# c -> money da?
# f -> pop karten, variable auf inaktiv
# allin -> an maximalem Geld der Spieler prüfen, splitpot für später
# konsole löschen
# bereitschaft usw.

# flop, turn, river
# wettrunde

# gewinnermittlung
# spielerposition wechseln
# (spieler austauschen/löschen/hinzufügen)
# neue Runde

# nach X Runden -> Blinds erhöhen
# nach Y Runden -> Endstatistik ausgeben