def divisione(n1,n2,i):
    if n1<n2:
        return i-1
    elif n1==n2:
        return i
    else:
        return divisione((n1-n2), n2,i+1)
        

i=1
n1=int(input("Inserisci dividendo: "))
n2=int(input("Inserisci divisore: "))
print(divisione(n1,n2,i))