class Automobile():
    
    modello = ""
    marca = ""
    colore = ""
    
    def __init__(self):
        self.modello = ""
        self.marca = ""
        
    def inserimento(self):
        marca = input("Inserisci la marca della macchina: ")
        self.marca = marca
        
        modello = input("Inserisci il modello della macchina: ")
        self.modello = modello
        
        colore = input("Inserisci il colore della macchina: ")
        self.colore = colore
        
    def __str__(self):
        return(f"marca: {self.marca}, modello: {self.modello}, colore: {self.colore}")