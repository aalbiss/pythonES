from Punto import *

p=Punto.origin()
print(p)
P1=Punto(1,2)
P2=Punto(3,4)
P3=Punto(0,0)
P4=Punto(0,0)
P5=Punto(6, 10)

P3=P3.puntoMedio(P1,P2)
print(P3)

P4=P1
P4=P4.puntoMedio2(P2)
print(P4)

print(f"Il quadrante del punto {P5} è {Punto.quadrante(P5)}") 


punto1 = Punto(2, 2)
punto2 = Punto(4, 6)

punto1.stampa_coordinate()
punto2.stampa_coordinate()

punto1.calcola_retta(punto2)

P5.appartieneAllaRetta(2, -2)