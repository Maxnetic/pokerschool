import spieler,tisch,karte
import os

#tisch erstellen
tisch = Tisch(...)
#spieler erstellen

tisch.Spielererstellung(...)

#karten erstellen und mischen
deck = tisch.deckErstellen()
gemischtesdeck = tisch.deckMischen(deck)

#liste von spielerobjekten, die in der position wechseln
spielerListe = tisch.spielerListe

#karten an spieler austeilen funktionerstellen
tisch.kartenAusteilen(spielerListe,gemischtesdeck)








#print aktuellen spielstatus: hand, eigenes geld, pot, aufgedeckte karten, verbliebene spieler usw.

#input aktion

# r -> wie viel?, auch bei anderen spielern da?
# c -> money da?
# f -> pop karten, variable auf inaktiv
# allin -> an maximalem Geld der Spieler prüfen, splitpot für später
# konsole löschen
konsoleLoeschen()
# bereitschaft usw.
spielerIndex = 0

for i in range(tisch.getSpielerAnzahl):
    
      print(spielerListe[spielerIndex].name)
      input("Sind Sie bereit?")
      print(spielerListe[0].getHand + tisch.zeigeSpielstaende() + " In der Mitte liegen " + tisch.getPot())
      input = input("möchten sie raisen (r), callen (c), folden (f) oder All in gehen (allin)")
      tisch.aktionVerarbeiten(input)


        
    
      spielerIndex = spielerIndex + 1

      

# flop, turn, river
tisch.flopaufdecken(deck)



# wettrunde - # Raise call fold funktion bauen
tisch.turnAufdecken(deck)
# wettrunde - # Raise call fold funktion bauen
tisch.riverAufdecken(deck)
# wettrunde - # Raise call fold funktion bauen

# gewinnermittlung Funktion schreiben zur Handbewertung

# Runde vorbei



# nächste Runde inizialiseren

# spielerposition wechseln
# (spieler austauschen/löschen/hinzufügen)
# neue Runde

# nach X Runden -> Blinds erhöhen
# nach Y Runden -> Endstatistik ausgeben

