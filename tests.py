import unittest
import tisch
import karte

class TestTisch(unittest.TestCase):

    def test_gemischt(self):    #Larissa
        pass
    
    def test_deckerstellt(self): # David
        pass

    def test_gemeinschaftskarten(self): # Dominic
        test_gk = tisch.Tisch()
        self.assertEqual(test_gk.Flop_aufdecken())
        self.assertEqual(test_gk.Turn_aufdecken())
        self.assertEqual(test_gk.River_aufdecken())


    def test_spieler_erstellt(self):    # Mikka
        pass

    def test_kartenausgeteilt(self): # Lucia
        pass

    def test_tischerstellt(self): # Moritz
        pass

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()