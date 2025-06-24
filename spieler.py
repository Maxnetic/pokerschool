class Spieler:
    def __init__(self, vermoegen, name, aktiv = True, kartenhand = 0,fertig = False):
        #der Spieler wird erstellt
        self.name = name
        self.kartenhand = kartenhand # Liste mit zwei Karten
        self.aktiv = aktiv
        self.vermoegen = vermoegen
        self.aktuellerEinsatz = 0
        self.fertig = fertig
        


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
 

    def Raise(self, betrag):
        #hier muss der Betrag dem Tisch zugeordnet werden
        #tisch.add_pot(betrag)
        #der Betrag wird dem vermögen abgezogen
        #TODO: verschieben zu Validierung Raise()  self.max_raises = 2       # Maximale Anzahl von Raises pro Runde, standardmäßig nach Pokerregeln bei 2
        if (self.vermoegen < betrag ):
            raise ValueError ('Der geforderte Einsatz ist groeßer als dein Vermögen.')
        else:
            self.vermoegen = self.vermoegen - betrag
            print('Der Einsatz wurde erhöht und beträgt nun:')
            print(self.betrag)
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
    
    def getVemoegen(self):
        return self.vermoegen


    def allIn(self, betrag):
        betrag = self.vermoegen
        self.vermoegen = 0
        return betrag
    

    def spielerFertig(self,fertig):
        self.fertig = fertig


    def getSpielerFertig(self):
        return self.fertig




    

   