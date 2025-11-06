print("Ana Eduarda, Byank, Emanuele, Guilherme.")
n=int(input("digite um número palíndromo: "))
s=str(n)
if s==s[::-1]:
    print("é polídromo!")
else:
    print("não é polídromo!")