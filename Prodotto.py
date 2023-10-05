def prodotto(n,m):
    if(m==0):
        return n
    else:
        return n*prodotto(m-1)+n
    
    
n=int(input("Inserisci n "))
m=int(input("Inserisci m "))
print(prodotto(n,m))