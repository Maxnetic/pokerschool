import unittest
from tisch import *

class TestTisch(unittest.TestCase):

    def test_gemischt(self):    #Larissa
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
            if neues_deck[i] == Karte(b, i):
                a = a + 1
                if a == 5:
                    raise ValueError("das Deck ist nicht gemischt")
    
    def test_deckerstellt(self): # David
        pass

    def test_gemeinschaftskarten(self): # Dominic
        pass

    def test_spieler_erstellt(self):    # Mikka
        a = Tisch()
        a.spielererstellung()
        self.assertEqual(len(a.spielerListe), int(input('vorher eingegebene Spieleranzahl:')))

    def test_kartenausgeteilt(self): # Lucia
        pass

    def test_tischerstellt(self): # Moritz
        pass

if __name__ == '__main__':
    unittest.main()

