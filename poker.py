from tisch import *
from spieler import *

#tisch erstellen
tisch1 = Tisch()
#spieler erstellen
tisch1.spielererstellung
#karten erstellen und mischen
tisch1.deckErstellen()
tisch1.deckMischen()
#karten an spieler austeilen
tisch1.handkartenAusteilen()
#liste von spielerobjekten, die in der position wechseln

for spielernummer in range(len(tisch1.spielerliste)):

    #print in die Konsole mit aktuellem Spieler
    print("Dieser Spieler ist jetzt dran: ")
    print(tisch1.spielerListe[spielernummer].name)
    #bereitschaft
    bereit = "etwas"
    while(bereit != ""):
        bereit = str(input("Zum Weitergehen drücke Enter"))
    #print aktuellen spielstatus: hand, eigenes geld, pot, aufgedeckte karten, verbliebene spieler usw.
    print("Deine Hand:" + tisch1.spielerListe[spielernummer].kartenhand)
    print("Dein Geld:" + tisch1.spielerListe[spielernummer].vermoegen)
    print("Pot:" + tisch1.pot)
    print("Aufgedeckte Karten:" + tisch1.gemeinschaftskarten)
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