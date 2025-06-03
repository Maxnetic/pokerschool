import unittest
from tisch import *

class TestTisch(unittest.TestCase):

    def testGemischt(self):    #Larissa
        a = 0 #zählt wieviele karten zufällig an der  richtigen stelle stehen
        b = 0 #zählt, die kartenfarbe abhängig von der stelle, an der man sich im deck befindet
        for i in range(57):
            if i <= 14:
                b = "pik"
            if i <= 28 and i > 14:
                b = "herz"
            if i <= 42 and i > 28:
                b = "karo"
            if i > 42:
                b = "kreuz"
            if neuesDeck[i] == Karte(b, i):
                a = a + 1
                if a == 5:
                    raise ValueError("das Deck ist nicht gemischt")
    
    def testDeckerstellt(self): # David
        pass

    def testGemeinschaftskarten(self): # Dominic
        pass

    def testSpielerErstellt(self):    # Mikka
        a = Tisch()
        a.spielererstellung()
        self.assertEqual(len(a.spielerListe), int(input('vorher eingegebene Spieleranzahl:')))

    def testKartenausgeteilt(self): # Lucia
        for i in range len(spielerListe): #Es wird getestet, ob ein Spieler in der Liste eine leere Liste hat.
            if (Spieler.kartenhand = 0):
                raise ValueError('Ein Spieler hat keine Karten')

    def testTischerstellt(self): # Moritz
        pass

    def testKartenattributeStimmen(self):       
    for i in range (len(deck)):         #testet für jede Karte im Stapel
        if (deck[i].farbe == '') or (deck[i].farbe != 'pik' and deck[i].farbe != 'karo' and deck[i].farbe != 'kreuz' and deck[i].farbe != 'herz'):
            i = str(i)
            raise ValueError("Die Kartenfarbe stimmt nicht an der Stelle: " + i)
        intWert = int(deck[i].wert)  #zum Testen ob der wert im bereich 2 - 14 liegt
        if (deck[i].wert == '') or (intWert < 2 or intWert > 14):
            i = str(i)
            raise ValueError("Der Kartenwert stimmt nicht an der Stelle: " + i)


    def testKartenWerdenAufgedeckt(self, wofuer):  
    if wofuer = "flop":
        if (len(gemeinschaftskarten) != 3):
            raise ValueError("Es werden zu viele oder zu wenige Karten für den Flop aufgedeckt")
    if wofuer = "turn":
        if (len(gemeinschaftskarten) != 4):
            raise ValueError("Es werden zu viele oder zu wenige Karten für den Turn aufgedeckt")
    if wofuer = "river":
        if (len(gemeinschaftskarten) != 5):
            raise ValueError("Es werden zu viele oder zu wenige Karten für den River aufgedeckt")

    def testWettrundeFunktioniert(self):
        pass

    def testHandbewertungStimmt(self):
        pass

    def testSpielendeWirdGeprueft(self):
        pass

    def testSpielerattributeStimmen(self):
        pass

    def testCallRaiseUndFoldFunktionieren(self):
        pass


if __name__ == '__main__':
    unittest.main()


    