from Automobile import * 

automobili = []

numeroMacchine = int(input("Inserisci il numero di macchine che vuoi inserire: "))
while(numeroMacchine<=0):
    numeroMacchine = int(input("Inserisci il numero di macchine che vuoi inserire: "))

for i in range(numeroMacchine):
    print(f"""Macchina {i+1}""")
    macchina=Automobile()
    macchina.inserimento()
    automobili.append(macchina)
    
for i in range(len(automobili)):
    print(f"""{i+1}: {macchina}""")
    
visualizzaMacchina = int(input("Inserisci il posto della macchina da visualizzare: "))
while(visualizzaMacchina<=0 or visualizzaMacchina>numeroMacchine):
    visualizzaMacchina = int(input("Inserisci il posto della macchina da visualizzare: "))

print(f"La macchina che si trova al posto {visualizzaMacchina} è {automobili[visualizzaMacchina-1]}")