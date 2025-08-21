somavalor= 0
contnegativo=0
for i in range (20):
    valor= int(input("Digite o valor: "))
    if valor >=0:
        somavalor= somavalor + valor
    else:
        contnegativo= contnegativo+1
    print("A soma dos valores positivos: ", somavalor)
    print("A quantidade de valores negativos é: ", contnegativo)
    