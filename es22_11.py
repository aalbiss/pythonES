#Creare una lista di N elementi int o float (N al max 20) ed effetturare le seguenti operazioni:
# 1) Visualizzare/stampare gli elementi di post pari
# 2) Media degli elementi divisibili per 3 o per 4
# 3) Ordinare il vettore di partenza
# 4) Caricare un secondo vettore della stessa dimensione del primo ed eseguire le seguenti operazioni: 
#      a. Somma, componente per componente dei 2 vettori
#      b. Differenza...
#      c. Inserisci uno scalare K (diverso da zero) e moltiplicare ogni elemento del vettore A per lo scalare 
#               A[3,5,6.-2] k = 6 --> [18, 30, 36, -12]
# 5) Fornire il max e il min del vettore B
# 6) Stampa il vettore B del contrario      B[4,6,2,10] --> [10,2,6,4]
# 7) concatena i vettori A e B

import random




def caricamento():   
    N = []
    for i in range(20):
        n=random.randint(1, 180)
        N.append(n)           
    return N

def visualizzaPari(N):
    somma = 0
    for i in range(len(N)):
        if (i%2 == 0):
            print(N[i], end=" ")
    
    

def media(N):
    somma = 0
    for i in range(len(N)):
        if (i%3 == 0) or (i%4 == 0):
            somma += N[i]
    media = somma/len(N)
    return media

def ordinamento(N):
    B = []
    for i in range(len(N)):
        B.append(N[i])
    B.sort()
    return B

# 4) Caricare un secondo vettore della stessa dimensione del primo ed eseguire le seguenti operazioni: 
#      a. Somma, componente per componente dei 2 vettori
#      b. Differenza...
#      c. Inserisci uno scalare K (diverso da zero) e moltiplicare ogni elemento del vettore A per lo scalare 
#               A[3,5,6.-2] k = 6 --> [18, 30, 36, -12]

def quattroA(N,A):
    B = []
    for i in range(len(N)):
        somma = N[i] + A[i]
        B.append(somma)
    return B

def quattroB(N, A):
    B = []
    for i in range(len(N)):
        B.append(N[i] - A[i])
    return B

# def quattroC()

def selezione(N):
    A = []
    for i in range(len(N)):
        n=random.randint(1, 180)
        A.append(n)
    print(" 1- Somma componente per componente: ")
    print(" 2- Differenza: ")
    print(" 3- Scalare: ")
    selezione = int(input("Inserisci operazione da fare"))
    while(selezione<0 or selezione>3):
        selezione = int(input("Inserisci operazione da fare"))
    if(selezione == 1):
        quattroA(N,A)
  
N = caricamento() 
                 
print(N)
print("--------")
visualizzaPari(N)
print("")
print("--------")
print(ordinamento(N))
print("--------")
print(selezione(N))
