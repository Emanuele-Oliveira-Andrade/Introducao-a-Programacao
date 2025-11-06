print("Ana Eduarda, Byank Chrystinny, Emanuele, Guilherme")
numero=int(input("Digite um número: "))
resto=0
resultado=0
while(numero%10!=0):
    resto=numero%10
    if (resto%2!=0):
        resultado=resultado+resto
    numero=numero//10
print("A soma dos números primos: ", resultado)