class Spieler:
    def __init__(self, vermoegen, name, aktiv = True, kartenhand = []):
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
        self.vermoegen = vermoegen - betrag

    def get_Hand(self): #Gibt die aktuelle Hand aus
        print('Hand: ' + self.kartenhand)

    # setzt die Kartenhand der Spieler. Spieler darf nicht mehr als zwei Karten besitzten.
    def set_Hand(self,karten):
        if(len(karten) > 2):
            print("Spieler darf nicht mehr als zwei Karten besitzen")


    def All_In(self, betrag):
        betrag = self.vermoegen
        self.vermoegen = 0
        return betrag

    