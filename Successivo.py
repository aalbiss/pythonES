#successivo
#S(0) = 1
#s(n) = n+1
#     = S(n-1)+1

def successivo(n):
    if(n==0):
        return 1
    else:
        return successivo(n-1)+1

n=int(input("Inserisci n "))
print(successivo(n))

#prodotto
# 3*4 3+3+3+3
#     |   |
#      3*3 +3

def prodotto(n,m):
    if(m==1):
        return n
    else:
        return prodotto(n,(m-1))+n
    
    
n=int(input("Inserisci n "))
m=int(input("Inserisci m "))
print(prodotto(n,m))