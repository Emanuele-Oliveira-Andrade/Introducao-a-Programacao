print("Ana Eduarda, Byank, Emanuele, Guilherme.")
n=int(input("Digite um número: "))
resto=0
binario=""
if n==0:
    binario="0"
else:
    while n>0:
        resto=n%2
        binario=str(resto)+binario
        n=n//2
print("o número em binario é:",binario)