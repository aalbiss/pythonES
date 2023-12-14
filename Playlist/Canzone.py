class Canzone():
    artista=""
    titolo=""
    durata=0
    genere=""

    def __init__(self):
        self.artista=""
        self.titolo=""
        self.durata=0
        self.genere=""
        
    def inserimento(self):
        self.artista=input("Inserisci artista: ")
        self.titolo=input("Inserisci titolo: ")
        self.durata=int(input("Inserisci durata: "))
        self.genere=input("Inserisci genere: ")
        
    def __str__(self):
        return (f"artista: {self.artista},titolo: {self.titolo},durata: {self.durata},genere: {self.genere}")
   