testoChiaro = input("Insersci il testo: ")
testoCifrato=""
#se il testo è in maiuscolo o minuscolo, tutto viene mantenuto, mantenere lo spazio
passo=int(input("Inserisci il passo: "))
while passo<3 or passo >10:
    passo=int(input("Inserisci il passo: "))
    
for i in testoChiaro:
    if(ord(i)+passo)>90:
        x=chr(ord(i)+passo-26)
    else:
        x=chr(ord(i)+passo)
        
    if(ord(i)+passo)>122:
        x=chr(ord(i)+passo-26)
    else:
        x=chr(ord(i)+passo)
        
    if ord(i)==32:
        x=chr(32)
    testoCifrato=testoCifrato+str(x)
    
print(testoCifrato)