import random
import time

start_time = time.time()

def caricamento(dim):
    A=[]
    for i in range(dim):
        x=random.randint(-20000,20000)
        A.append(x)
    return A

def bubbleSort(A):
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[j]<A[i]:
                A[i],A[j]=A[j],A[i]
    
    for i in range(len(A)):
        print(A[i], end=", ")
    
dim=int(input("Quanti elementi vuoi inserire? "))

print(bubbleSort(caricamento(dim)))
print(time.time() - start_time)
