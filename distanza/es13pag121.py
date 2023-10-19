import math

def punto():
    x=float(input("insersici ascissa: "))
    y=float(input("inserisci ordinata: "))
    return x,y

def distanza(x1,y1,x2,y2):
    d=math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
    return d