a=0
b=0
c=0
print("Aplicação de operações matemáticas")
print("Escolha uma das operações matemáticas:")
print("1- Soma")
print("2- Subtração")
print("3- Multiplicação")
print("4- Divisão")
print("5- Par ou ímpar")
print("6- Fatorial")
print("7- Primo")
resposta= (input("Escolha qual operação matemática deseja usar, colocando o número da operação (caso queira sair, escreva 'SAIR'): "))
while resposta!=("SAIR"):
    if resposta== 1:
        a=(int(input("Primeiro número: ")))
        b=(int(input("Segundo número: ")))
        print(a+b)
    if resposta == 2:
        a=(int(input("Primeiro número: ")))
        b=(int(input("Segundo número: ")))
        print(a-b)
    if resposta == 3:
        a=(int(input("Primeiro número: ")))
        b=(int(input("Segundo número: ")))
        print(a*b)
    if resposta == 4:
        a=(int(input("Primeiro número: ")))
        b=(int(input("Segundo número: ")))
        print(a/b)
    if resposta == 5:
        a=(int(input("Primeiro número: ")))
        if a % 2 !=0:
            print("O número é ímpar")
        else: 
            print("O número é par")
    if resposta == 4:
        a=(int(input("Primeiro número: ")))
        b=(int(input("Segundo número: ")))
        print(a/b)