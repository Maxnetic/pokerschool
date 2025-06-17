from tisch import *

class Spieler:
    def __init__(self, vermoegen, name, platz, aktiv = True, kartenhand = 0):
        #der Spieler wird erstellt
        self.name = name
        self.kartenhand = kartenhand # Liste mit zwei Karten
        self.aktiv = aktiv
        self.vermoegen = vermoegen
        self.tisch = platz

    def call(self, betrag):
        #hier muss der betrag dem Tisch zuaddiert werden
        #tisch.add_pot(betrag)
        #das Vermögen wird gesengt
        if(self.vermoegen < betrag):
            self.fold
        else:
            self.vermoegen = self.vermoegen - betrag   

    def fold(self):
        #hier muss der Spieler aus der Liste der Beteiligten gelöscht werden
        #Der Status wird auf raus gesetzt
        self.aktiv = False
        return self.aktiv

    def Raise(self, betrag):
        #hier muss der Betrag dem Tisch zugeordnet werden
        #tisch.add_pot(betrag)
        #der Betrag wird dem vermögen abgezogen
        if (self.vermoegen < betrag ):
            self.fold()
        
        self.platz.add_pot(betrag)
        self.platz.add_aktuelleWette(betrag)
        self.vermoegen = self.vermoegen - betrag     #TODO: Betrag dem pot hinzufügen
        print('Der Einsatz wurde erhöht und beträgt nun:')
        print(self.betrag)

    def getHand(self): #Gibt die aktuelle Hand aus
        print('Hand: ' + self.kartenhand)

    # Kartenhand als Liste. Default leere Liste
    def setHand(self, karten = []):
        #validieren,sodass es sich um wirklich zwei Karten handelt.
        if(len(karten) != 2):
            print("Fehler")
        self.kartenhand = karten


    def allIn(self, betrag):
        betrag = self.vermoegen
        self.vermoegen = 0
        return betrag

    

   