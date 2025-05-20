import unittest
from tisch import *

class TestTisch(unittest.TestCase):

    def test_gemischt(self):    #Larissa
        pass
    
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

