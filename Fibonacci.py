def fibonacciIte(n):
    A=[]
    A.append(0)
    A.append(1)
    for i in range (2, n):
        A.append(A[i-1]+A[i-2])
    return A


def fibonacciRic(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        n = fibonacciRic(n-1)+fibonacciRic(n-2)
        return n
    

print("1- Fibonacci Iterativo")  
print("2- Fibonacci Ricorsivo")
s=int(input("Scegliere quale fibonacci usare"))
    
n=int(input("Inserisci n: "))

if(s==1):
    print(f"""{fibonacciIte(n)}""")
elif(s==2):
    for i in range(0, n):
        print(f"""{i} : {fibonacciRic(i)}""")