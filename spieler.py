class Spieler:
    def __init__(self, vermoegen, name, aktiv = True, kartenhand = 0):
        #der Spieler wird erstellt
        self.name = name
        self.kartenhand = kartenhand # Liste mit zwei Karten
        self.aktiv = aktiv
        self.vermoegen = vermoegen

    def Call(self, betrag):
        #hier muss der betrag dem Tisch zuaddiert werden
        #tisch.add_pot(betrag)
        #das Vermögen wird gesengt
        if(self.vermoegen < betrag):
            raise ValueError ('Der geforderte Einsatz ist groeßer als dein Vermögen.')
        else:
            self.vermoegen = self.vermoegen - betrag
            return self.vermoegen    

    def Fold(self):
        #hier muss der Spieler aus der Liste der Beteiligten gelöscht werden
        #Der Status wird auf raus gesetzt
        self.aktiv = False
        return self.aktiv

    def Raise(self, betrag):
        #hier muss der Betrag dem Tisch zugeordnet werden
        #tisch.add_pot(betrag)
        #der Betrag wird dem vermögen abgezogen
        #TODO: verschieben zu Validierung Raise()  self.max_raises = 2       # Maximale Anzahl von Raises pro Runde, standardmäßig nach Pokerregeln bei 2
        if (self.vermoegen < betrag ):
            raise ValueError ('Der geforderte Einsatz ist groeßer als dein Vermögen.')
        else:
            self.vermoegen = vermoegen - betrag
            print('Der Einsatz wurde erhöht und beträgt nun:')
            print(self.betrag)
            return betrag

    def get_Hand(self): #Gibt die aktuelle Hand aus
        print('Hand: ' + self.kartenhand)

    # Kartenhand als Liste. Default leere Liste
    def set_Hand(karten = []):
        #validieren,sodass es sich um wirklich zwei Karten handelt.
        if(len(karten) != 2):
            print("Fehler")
        self.kartenhand = karten


    def All_In(self, betrag):
        betrag = self.vermoegen
        self.vermoegen = 0
        return betrag

    

   