from tisch import *; from spieler import *; from karte import *

def aktion(self):
    zug = input('Was möchtest du tun? (r/c/f/allin)')
    if(zug != 'r' or 'c' or 'f' or 'allin'):
        zug = input('Das ist nicht möglich. Was möchtest du tun? (r/c/f/allin)')
    elif(zug == 'r'):
        tisch1.spielerListe[i].Raise
    elif(zug == 'c'):
        tisch1
    else:
        pass
def spielverlauf(self):
    print(f"Hand: {tisch1.spielerListe[i].kartenhand}, aktuelles Vermögen: {tisch1.spielerListe[i].vermögen}, der pot: {tisch1.pot}")
    print(f'Die verbliebenen Spieler sind: {[print (Spieler.name) for i in range(len(tisch1.spielerListe))]}')
    print(f'Die aufgedeckten Karten sind: {tisch1.gemeinschaftskarten}')      #Das sind die Stats, die man vor dem Spielbeginn braucht.  

#tisch erstellen
tisch1 = Tisch()
#spieler erstellen:
tisch1.spielerErstellen()
#karten erstellen und mischen
tisch1.deckErstellen()
tisch1.deckMischen()
#karten an spieler austeilen
tisch1.kartenAusteilen()
#liste von spielerobjekten, die in der position wechseln
tisch1.flopAufdecken()
#print in die Konsole mit aktuellem Spieler
print('Der aktuelle Spieler ist: '+ tisch1.spielerListe[0])

for i in range (len(tisch1.spielerListe)):
    bereitschaft = input(tisch1.spielerListe[i] + ' bist du bereit?')
    if(bereitschaft != ('ja' or 'Ja')):
        bereitschaft = input(tisch1.spielerListe[i] + ' bist du bereit?')
    else:
       spielverlauf() 
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