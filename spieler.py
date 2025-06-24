from tisch import *

class Spieler:
    def __init__(self, vermoegen, name, aktiv = True, kartenhand = 0, fertig = False, tisch = None):
        #der Spieler wird erstellt
        self.name = name
        self.kartenhand = kartenhand # Liste mit zwei Karten
        self.aktiv = aktiv
        self.vermoegen = vermoegen
        self.aktuellerEinsatz = 0
        self.letzteAktion = None
        self.tisch = tisch
        
        #hier muss der betrag dem Tisch zuaddiert werden
        #tisch.add_pot(betrag)
        #das Vermögen wird gesengt
    def call(self, betrag):
        
        if(self.vermoegen < betrag):
            raise ValueError ('Der geforderte Einsatz ist groeßer als dein Vermögen.')
        else:
             self.vermoegen = self.vermoegen - betrag
        
        return betrag


          

    def fold(self):
        #hier muss der Spieler aus der Liste der Beteiligten gelöscht werden
        #Der Status wird auf raus gesetzt
        self.aktiv = False
 

    def Raise(self):
        betrag = int(input("Um wie viel wollen Sie die aktuelle Wette erhöhen?"))
        if (self.vermoegen < betrag ):
            print('Der geforderte Einsatz ist groeßer als dein Vermögen.')
            self.Raise()
        #elif ():
            # TODO theoretisch nur Raise bis Vermögen von ärmstem Spieler
        else:
            self.vermoegen = self.vermoegen - betrag
            self.aktuellerEinsatz = self.aktuellerEinsatz + betrag
            self.tisch.aktuelleWette = self.aktuellerEinsatz
            print('Der Einsatz wurde erhöht und beträgt nun:')
            print(self.aktuellerEinsatz)
            # alle anderen fertig auf false setzten in Tisch
        
        return betrag
    
    
    
    def allIn(self):
        betrag = self.vermoegen
        self.vermoegen = 0
        self.fertig = True
        return betrag
        
            

    def getHand(self): #Gibt die aktuelle Hand aus
        print('Hand: ' + self.kartenhand)

    # Kartenhand als Liste. Default leere Liste
    def setHand(self, karten = []):
        #validieren,sodass es sich um wirklich zwei Karten handelt.
        if(len(karten) != 2):
            print("Fehler")
        self.kartenhand = karten

    def getName(self):
        return self.name
    
    def getVermoegen(self):
        return self.vermoegen

    def allIn(self, betrag):
        betrag = self.vermoegen
        self.vermoegen = 0
        return betrag

    def getInfo(self):
        print("aufgedeckte Karten: " + self.tisch.getGemeinschaftskarten())                         #ausgeben der zum zeitpunkt wichtigen daten
        print("Hand: " + self.getHand())
        print("Vermögen: " + self.getVermoegen)
        #Geld im Pot
        #Aktuelle Wette
        #Eigene Wette
        #Namen der anderen Spieler und deren Vermögen?
        #Blinds
        #Rundenanzahl
        #Status der anderen Spieler/letzte Aktion der anderen Spieler





    

   