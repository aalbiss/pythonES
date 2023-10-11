def risoluzione(a,b):
    risposta=""
    if a==0 and b==0:
        risposta="Indeterminata"
    elif a==0 and b!=0:
        risposta="Impossibile"
    elif a!=0 and b==0:
        risposta=0
    else:
        risposta=-(b/a)
    return risposta
    
a=int(input("Inserisci a: "))
b=int(input("Inserisci b: "))
print(f""" {a}x+{b} = 0""")
print(f"""x = {risoluzione(a,b)}""")