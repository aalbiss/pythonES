import random

def classe(a,b,c,d):
    print(f"""Il tuo indirizzo IP è: {a}.{b}.{c}.{d}""")
    if a >= 1 and a <= 127:
        print("Classe A")
        print(f"""IP : {a}.{b}.{c}.{d}/8""")
        print("SubnetMask: 255.0.0.0")
    elif a >= 128 and a <= 191:
        print("Classe B")
        print(f"""IP : {a}.{b}.{c}.{d}/16""")
        print("SubnetMask: 255.255.0.0")
    elif a >= 192 and a <= 223:
        print("Classe C")
        print(f"""IP : {a}.{b}.{c}.{d}/24""")
        print("SubnetMask: 255.255.255.0")
    elif a >= 224 and a <= 239:
        print("Classe D")
        print(f"""IP : {a}.{b}.{c}.{d}""")
    elif a >= 240 and a <= 255:
        print("Classe E")
        print(f"""IP : {a}.{b}.{c}.{d}""")
    else:
        print("Indirizzo IP non valido")
        
def submaskClassi(ott):
    subnet = ""
    if ott>=1 and ott<=127:
        for i in range(1, 9):
            subnet += "1"
            if i % 8 == 0:
                subnet += "."

        for i in range(1, (32 - 8) + 1):
            subnet += "0"
            if i % 8 == 0:
                subnet += "."

    elif ott >= 128 and ott <= 191:
        for i in range(1, 17):
            subnet += "1"
            if i % 8 == 0:
                subnet += "."

        for i in range(1, (32 - 16) + 1):
            subnet += "0"
            if i % 8 == 0:
                subnet += "."

    elif ott >= 192 and ott <= 223:
        for i in range(1, 25):
            subnet += "1"
            if i % 8 == 0:
                subnet += "."

        for i in range(1, (32 - 24) + 1):
            subnet += "0"
            if i % 8 == 0:
                subnet += "."

    elif ott >= 224 and ott <= 255:
        for i in range(1, 33):
            subnet += "1"
            if i % 8 == 0:
                subnet += "."

    subnet = subnet[:len(subnet) - 1]
    return subnet

def submMaskVariabile():
    submask = int(input("Inserisci la submask: "))
    while (submask > 30):
        print("La submask deve essere minore o uguale di 30")
        submask = int(input("Reinserire la submask: "))
    print("-----------------------------------------------------")
    print(f"""Il tuo indirizzo IP è: {a}.{b}.{c}.{d}/{submask}""")
    
    n = 0
    subnet = ""
    subnetDec = ""
    k = 0
    l = 0
    F = []
    A = []
    for i in range(1, submask + 1):
        subnet += "1"
        n += 1
        if n % 8 == 0:
            subnet += "."
            k+=1
    A.clear()
    F.clear()
    k = 0
    for i in range(1, (32 - submask) + 1):
        subnet += "0"
        n += 1
        if n % 8 == 0:
            subnet += "."
            k += 1    
            
    subnet = subnet[:len(subnet) - 1]
    A  = subnet.split(".", 4)
      
    for i in range(len(A)):
        l = int(A[i], 2)
        subnetDec = subnetDec + str(l) + "."
                
    subnetDec = subnetDec[:len(subnetDec) - 1]
    print(f"""La subnet mask binaria è {subnet}  \nLa subnet mask decimale è {subnetDec} """)


a = random.randint(0, 255)
b = random.randint(0, 255)
c = random.randint(0, 255)
d = random.randint(0, 255)

submMaskVariabile()
