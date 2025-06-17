import spieler,tisch,karte, os
from tisch import Tisch, SpielerListe, aktuelleWette, raiseCount
from spieler import Spieler
#tisch erstellen
tisch = Tisch()
#spieler erstellen
tisch.spielererstellung()
#karten erstellen und mischen
deck = tisch.deckErstellen()
gemischtesDeck = tisch.deckMischen(deck)
#karten an spieler austeilen
pass
#liste von spielerobjekten, die in der position wechseln
pass #(vorhanden)
#print aktuellen spielstatus: hand, eigenes geld, pot, aufgedeckte karten, verbliebene spieler usw.
tisch.zeigeSpielstaende()
#print in die Konsole mit aktuellem Spieler
for spieler in SpielerListe:
#bereitschaft
    print({Spieler[0]} + ", drücke Enter, um deine Karten zu sehen.")
#print aktuellen spielstatus: hand, eigenes geld, pot, aufgedeckte karten, verbliebene spieler usw.
    tisch.zeigeSpielstaende()
    tisch.getHand(Spieler[0])
#input aktion
    eingabe = input(print("Möchtest du raisen (r), callen (c), folden (f) oder all-in gehen (allin)?"))
# r -> wie viel?, auch bei anderen spielern da?
    if eingabe == "r":
        erhöhung = int(input(print("Erhöhungsbetrag:")))
        aktuelleWette = aktuelleWette + erhöhung
        raiseCount = raiseCount + 1
        tisch.Raise(aktuelleWette)
        print(Spieler[0] + "hat um den Betrag" + erhöhung + "geraist.")
# c -> money da?
    elif eingabe == "c":
        tisch.Call()
        print(Spieler[0] + "hat gecallt.")
# f -> pop karten, variable auf inaktiv
    elif eingabe == "f":
        tisch.Fold()
        print(Spieler[0] + "hat gefoldet.")
# allin -> an maximalem Geld der Spieler prüfen
    elif eingabe == "allin":
        tisch.allIn()
        print(Spieler[0] + "ist all-in gegangen.")
# konsole löschen
    os.system('cls' if os.name == 'nt' else 'clear')
    Spieler[0] = Spieler[1] 

# flop, turn, river
tisch.flopAufdecken(gemischtesDeck)
tisch.turnAufdecken(gemischtesDeck)
tisch.riverAufdecken(gemischtesDeck)
# wettrunde

# gewinnermittlung
# spielerposition wechseln
# (spieler austauschen/löschen/hinzufügen)
# neue Runde

# nach X Runden -> Blinds erhöhen
# nach Y Runden -> Endstatistik ausgeben