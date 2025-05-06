class Spieler:
    def __init__(self, vermoegen, name, aktiv = True, kartenhand = 0):
        #der Spieler wird erstellt
        self.name = name
        self.kartenhand = kartenhand
        self.aktiv = aktiv
        self.vermoegen = vermoegen

    def Call(self, betrag):
        #hier muss der betrag dem Tisch zuaddiert werden
        #tisch.add_pot(betrag)
        #das Vermögen wird gesengt
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
        self.vermoegen = vermoegen - betrag

    def get_Hand(self): #Gibt die aktuelle Hand aus
        print('Hand: ' + self.kartenhand)

    def All_In(self, betrag):
        betrag = self.vermoegen
        self.vermoegen = 0
        return betrag

    def kartenausteilen(self, karten):
        #der Tisch greift auf dise Methode beim Kartenausteilen zu
        self.kartenhand = karten
        return self.kartenhand