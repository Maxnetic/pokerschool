import unittest
from tisch import *
from karte import *
from spieler import *

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
            if Tisch.neuesDeck[i] == Karte(b, i):
                a = a + 1
                if a == 5:
                    raise ValueError("das Deck ist nicht gemischt")
    
    def testDeckerstellt(self): # David
        pass

    def testGemeinschaftskarten(self): # Dominic
        tisch = Tisch()
        deck = tisch.deckErstellen()
        gemischtesDeck = tisch.deckMischen(deck)
        ursprungslaenge = len(gemischtesDeck)
    
        # Flop
        tisch.flopAufdecken(gemischtesDeck)
        self.assertEqual(len(tisch.gemeinschaftskarten), 3, "Flop sollte 3 Karten aufdecken.")
        self.assertEqual(len(gemischtesDeck), ursprungslaenge - 3, "Deck sollte um 3 Karten reduziert werden.")

        # Turn
        tisch.turnAufdecken(gemischtesDeck)
        self.assertEqual(len(tisch.gemeinschaftskarten), 4, "Turn sollte eine Karte hinzufügen.")
        self.assertEqual(len(gemischtesDeck), ursprungslaenge - 4, "Deck sollte um 4 Karten reduziert sein.")

        # River
        tisch.riverAufdecken(gemischtesDeck)
        self.assertEqual(len(tisch.gemeinschaftskarten), 5, "River sollte eine Karte hinzufügen.")
        self.assertEqual(len(gemischtesDeck), ursprungslaenge - 5, "Deck sollte um 5 Karten reduziert sein.")

        ''' Überprüfen, ob alle Gemeinschaftskarten eindeutig sind (optional)
        karten_str = [str(karte) for karte in tisch.gemeinschaftskarten]
        self.assertEqual(len(karten_str), len(set(karten_str)), "Gemeinschaftskarten enthalten Duplikate.")'''


    def testSpielerErstellt(self):    # Mikka
        a = Tisch()
        a.spielererstellung()
        self.assertEqual(len(a.spielerListe), int(input('vorher eingegebene Spieleranzahl:')))

    def testKartenausgeteilt(self): # Lucia
        for i in range (len(tisch.spielerListe)): #Es wird getestet, ob ein Spieler in der Liste eine leere Liste hat.
            if (Spieler.kartenhand == 0):
                raise ValueError('Ein Spieler hat keine Karten')

    def testTischerstellt(self): # Moritz
        pass

    def testKartenattributeStimmen(self):       
        for i in range (len(Tisch.deck)):         #testet für jede Karte im Stapel
            if (Tisch.deck[i].farbe == '') or (Tisch.deck[i].farbe != 'pik' and Tisch.deck[i].farbe != 'karo' and Tisch.deck[i].farbe != 'kreuz' and Tisch.deck[i].farbe != 'herz'):
                i = str(i)
                raise ValueError("Die Kartenfarbe stimmt nicht an der Stelle: " + i)
            intWert = int(Tisch.deck[i].wert)  #zum Testen ob der wert im bereich 2 - 14 liegt
            if (Tisch.deck[i].wert == '') or (intWert < 2 or intWert > 14):
                i = str(i)
                raise ValueError("Der Kartenwert stimmt nicht an der Stelle: " + i)


    def testKartenWerdenAufgedeckt(self, wofuer):  
        if wofuer == "flop":
            if (len(Tisch.gemeinschaftskarten) != 3):
                raise ValueError("Es werden zu viele oder zu wenige Karten für den Flop aufgedeckt")
        if wofuer == "turn":
            if (len(Tisch.gemeinschaftskarten) != 4):
                raise ValueError("Es werden zu viele oder zu wenige Karten für den Turn aufgedeckt")
        if wofuer == "river":
            if (len(Tisch.gemeinschaftskarten) != 5):
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


    