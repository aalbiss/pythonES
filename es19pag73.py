#programma che accetti i numeri finchè non viene inserito il numero 0
import random

def creazioneNumeri():
    V=[]
    n=random.randint(0,100)
    if(n!=0):
        V.append(n)
    while(n!=0):
        n=random.randint(0,100)
        if(n!=0):
            V.append(n)
    return V
    
def visualizza(V):
    print(V)
    print(len(V))
    
visualizza(creazioneNumeri())