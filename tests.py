import unittest

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