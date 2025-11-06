print("Ana Eduarda, Byank Chrystinny, Emanuele, Guilherme.")
numero= int(input("Digite um número: "))
quantidade_impares=0
while (numero>0):
    resto=numero%10
    if (resto%2!=0):
        quantidade_impares+=1
    numero= numero//10
fatorial=1
for i in range(1, quantidade_impares+1):
    fatorial*=i
print("O fatorial dos número ímpares é: ", fatorial)