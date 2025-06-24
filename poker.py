from spieler import *
from tisch import * 
from karte import *
import os

#tisch erstellen
tisch = Tisch()

#spieler erstellen
tisch.spielererstellung()

#karten erstellen und mischen
deck = tisch.deckErstellen()
deck = tisch.deckMischen(deck)

#karten an spieler austeilen funktionerstellen
tisch.kartenAusteilen(tisch.spielerListe, deck)

# r -> wie viel?, auch bei anderen spielern da?
# c -> money da?
# f -> pop karten, variable auf inaktiv
# allin -> an maximalem Geld der Spieler prüfen, splitpot für später
# konsole löschen
# bereitschaft usw.
# spieler nicht fertig

for i in tisch.rundenanzahl:
    print("Runde " + str(i))
    for spieler in tisch.spielerListe:
        input(str(spieler.getName()) + " sind Sie bereit? Drücken Sie Enter")
        spieler.getInfo() #Infos vom Tisch und vom aktuellen Spieler anzeigen
        aktion = input("Möchten sie raisen (r), callen (c), folden (f) oder All in gehen (allin)")
        tisch.aktionVerarbeiten(aktion, spieler)

# flop, turn, river
tisch.flopaufdecken(deck)
# auslagern in Methode



# wettrunde - # Raise call fold funktion bauen
tisch.turnAufdecken(deck)

# wettrunde - # Raise call fold funktion bauen
tisch.riverAufdecken(deck)



# gewinnermittlung Funktion schreiben zur Handbewertung

# Runde vorbei



# nächste Runde inizialiseren

# spielerposition wechseln
# (spieler austauschen/löschen/hinzufügen)
# neue Runde

# nach X Runden -> Blinds erhöhen
# nach Y Runden -> Endstatistik ausgeben



def legeSmallUndBigBlindFest(spielerListe):
      # erstmal vereinfachen
      