texto=input ("Ingrese un texto:  ")

if texto==texto.upper(): 
    abecedario="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
else:
    abecedario="abcdefghijklmnñopqrstuvwxyz"
k=int (input ("Valor de desplazamiento: "))

cifrado=""
for c in texto:
    if c in abecedario:
        cifrado += abecedario[(abecedario.index(c)+k%(len(abecedario)))]
    else:
        cifrado+=c 
print("texto cifrado: ",cifrado)