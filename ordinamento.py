#Da una lista eliminare i doppioni A=[3,5,2,3,7,3,2]  INPUT
#                                    [3,2,5,7]        OUTPUT

#                           BUBBLE SORT
import random

def caricamento():
    A=[]
    for i in range (30):
        x=random.randint(1,15)
        A.append(x)
    return A
    
def ordinamento(A):
    for i in range(len(A)):
        for j in range(i+1,len(A), 1):
            if(A[j]<A[i]):
                A[j],A[i]=A[i],A[j]
    return A

def ordinamentoSort(A):
    A.sort()
    return A
        
def eliminazioneDoppioni(A):
    for i in range(len(A)):
        for j in range(i+1,len(A), 1):
            if(A[j]==A[i]):
                A.pop(j)
                print(A)
    

print(ordinamento(caricamento()))
print(eliminazioneDoppioni(caricamento()))

