#programma che accetti da tastiera un elenco di n prezzi e li sommi.
#Fornire il totale dei prezzi

def totale_prezzi(A):
    somma=0
    for i in range(len(A)):
       somma+=A[i]
    return somma
       
def prezzi(n):
    A=[]
    for i in range(n):
        prezzo=int(input(f"""inserisci il prezzo {i+1}: """))
        A.append(prezzo)
    return A
      
n=int(input("Quanti prodotti vuoi inserire? "))
while(n<=0):
    N=int(input("Quanti prodotti vuoi inserire"))
print(totale_prezzi(prezzi(n)))