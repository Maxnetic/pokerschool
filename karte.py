class Karte:
    def __init__(self,farbe,wert):
        self.farbe = farbe
        self.wert = wert       
    
    def getFarbe(self):
        return self.farbe
    
    def getWert(self):
        return self.wert
    
    def printWert(self):  #StringWert ist ein Dictionary, das den Werten 11 bis 14 Namen zuordnet
        stringWert = {
            11: 'Bube',
            12: 'Dame',
            13: 'König',
            14: 'Ass'}
        wertAlsString = stringWert.get(self.wert, str(self.wert)) #Wenn der Wert im Dictionary vorkommt, wird er ausgegeben, sonst der Wert als String
        return f"{self.farbe} {wertAlsString}"

    def __str__(self): # Wird aufgerufen, wenn print() aufgerufen wird
        return f"{self.farbe} {self.wert}"

    def __repr__(self): # Sonst werden Speicheradressen und keine Namen ausgegeben
        return self.__str__()
    
