class Spieler:
    def __init__(self, vermoegen, name, aktiv = True, karten_hand = 0):
        #der Spieler wird erstellt
        self.name = name
        self.karten_hand = karten_hand # Liste mit zwei Karten
        self.aktiv = aktiv
        self.vermoegen = vermoegen

    def call(self, betrag):
        #hier muss der betrag dem Tisch zuaddiert werden
        #tisch.add_pot(betrag)
        #das Vermögen wird gesengt
        self.vermoegen = self.vermoegen - betrag
        return self.vermoegen

    def fold(self):
        #hier muss der Spieler aus der Liste der Beteiligten gelöscht werden
        #Der Status wird auf raus gesetzt
        self.aktiv = False
        return self.aktiv

    def lift(self, betrag):
        #hier muss der Betrag dem Tisch zugeordnet werden
        #tisch.add_pot(betrag)
        #der Betrag wird dem vermögen abgezogen
        self.vermoegen = vermoegen - betrag

    def get_hand(self): #Gibt die aktuelle Hand aus
        print('Hand: ' + self.karten_hand)

    # Kartenhand als Liste. Default leere Liste
    def set_hand(karten = []):
        #validieren,sodass es sich um wirklich zwei Karten handelt.
        if(len(karten) != 2):
            print("Fehler")
        self.karten_hand = karten


    def all_in(self, betrag):
        betrag = self.vermoegen
        self.vermoegen = 0
        return betrag

    

   