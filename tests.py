import unittest

class TestTisch(unittest.TestCase):

    def test_gemischt(self):    #Larissa
        pass
    
    def test_deckerstellt(self): # David
        pass

    def test_gemeinschaftskarten(self): # Dominic
        pass

    def test_spieler_erstellt(self):    # Mikka
        pass

    def test_kartenausgeteilt(self): # Lucia
        for i in range len(spielerListe): #Es wird getestet, ob ein Spieler in der Liste eine leere Liste hat.
            if (Spieler.kartenhand = 0):
                raise ValueError('Ein Spieler hat keine Karten')

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