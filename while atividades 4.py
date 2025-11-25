n= int(input("Digite um número (0 para sair): "))
resultado=0
while n!=0:
    resultado+=n
    n= int(input("Digite um número (0 para sair): "))
print("A soma de todos os números digitados é: ", resultado)