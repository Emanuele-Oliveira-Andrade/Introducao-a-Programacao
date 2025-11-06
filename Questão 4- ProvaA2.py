# Guilherme Carrijo, Emanuele, Ana e Byank
numero= int(input("Digite um número: "))
resto=0
resultado=0
quantidadededigitos=0
while (numero%10!=0):
    resto= numero%10
    resultado+=resto
    numero=numero//10
    quantidadededigitos+=1
media=resultado/quantidadededigitos
print(media)

