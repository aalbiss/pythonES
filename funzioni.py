def nomiKM(N):
    nomiKM=[[],[]]
    for i in range(N):
        nomiKM[0].append(input("Inserisci nome: ")) 
        nomiKM[1].append(int(input("Inserisci kilometri: ")))
    return nomiKM


def stampa(nomiKM,n):
    for i in range(n):
        if(nomiKM[1][i] >=30):
            print(nomiKM[0][i], end=" ")