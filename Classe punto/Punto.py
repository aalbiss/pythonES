class Punto:
    @classmethod
    def origin(cls):
        return cls(0,0)
        
    def __init__(self, x= 0, y = 0):
        self.x = x
        self.y = y

    def stampa_coordinate(self):
        print(f"({self.x} , {self.y})")

    def puntoMedio(self, p1, p2):
        return Punto((p1.x + p2.x)/2, (p1.y + p2.y)/2)

    def __str__ (self):
        return f"({self.x}, {self.y})"

    def puntoMedio2(self, target):
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Punto(mx, my)

    def calcola_retta(self, altro_punto):
        if self.x == altro_punto.x:
            #La retta è verticale, non è possibile calcolare il coefficente angolare
            print("La retta è verticale e non ha un coefficiente angolare definito.")
        else:
            # Calcola il coefficiente angolare (pendenza) della retta
            m = (altro_punto.y - self.y) / (altro_punto.x - self.x)
            # Calcola l'intercetta y della retta
            q = self.y - m * self.x
            
            print(f"Equazione della retta: y = {m}x + {q}")    
        
    def quadrante(self):
        if self.x > 0 and self.y > 0:
            return "I° quadrante"
        elif self.x < 0 and self.y > 0:
            return "II° quadrante"
        elif self.x < 0 and self.y < 0:
            return "III° quadrante"
        elif self.x > 0 and self.y < 0:
            return "IV° quadrante"
        elif self.x==0 or self.y==0:
            return "E' sull'asse"
        else:
            return "Origine"
        
    def appartieneAllaRetta(self, m, q):
        if self.y == (m*self.x + q):
            print("Il punto appartiene alla retta")
        else:
            print("Il punto non appartiene alla retta")
         