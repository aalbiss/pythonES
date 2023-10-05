#programma che accetti da tastiera un elenco di n prezzi e li sommi.
#Fornire il totale dei prezzi
def totale_prezzi(A):
    somma=0
    for i in range(len(A)):
       somma+=A[i]
    return somma
       
def prezzi(A):
    prezzo=int(input(f"""inserisci il prezzo """))
    A.append(prezzo)
    return A

def inserimento():
    A=[]
    i=1
    prezzi(A)
    n=input("Vuoi inserire un altro prezzo? ")
    while n=="s":
        i+=1
        prezzi(A)
        n=input("Vuoi inserire un altro prezzo? ")
    print(totale_prezzi(A))
        
inserimento()
   