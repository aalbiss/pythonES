def inserimentoVoti():
    nomiVoti=[[],[]]
    for i in range(2):
        nomiVoti[0].append(input("Inserisci nome: "))
        voto=int(input("Inserisci voto: "))
        while(voto>=19):
            voto=int(input("Inserisci voto: "))
        nomiVoti[1].append(voto)
    return nomiVoti
# def percentualeOttenuta()