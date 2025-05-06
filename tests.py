from spieler import Spieler

def Spielertest():
    a = Spieler(100, "Mikka")
    assert a.name == "Mikka"

def test_karte():
    #assert
    pass

Spielertest()