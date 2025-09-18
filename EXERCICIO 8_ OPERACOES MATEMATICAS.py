aa=0
b=0
c=0
fatorial=1
print("********** OPERAÇÕES MATEMÁTICAS **********")
print("Escolha uma das operações matemáticas abaixo. Para encerrar digite 'SAIR' :")
print("1- Soma")
print("2- Subtração")
print("3- Multiplicação")
print("4- Divisão")
print("5- Par ou ímpar")
print("6- Fatorial")
print("7- Primo")
resposta= (input("Escolha qual operação matemática deseja usar, colocando o número da operação ou <SAIR> para encerrar: "))
respostaMaiusculo=resposta.upper()
while resposta!="SAIR" or "Sair" or "sair":
    if resposta== "1":
        a=(int(input("Primeiro número: ")))
        b=(int(input("Segundo número: ")))
        print("O resultado da soma é ", a+b)
        input("Pressione ENTER para voltar ao MENU! ")
    if resposta == "2":
        a=(int(input("Primeiro número: ")))
        b=(int(input("Segundo número: ")))
        print("A subtração é ", a-b)
        input("Pressione ENTER para voltar ao MENU! ")
    if resposta == "3":
        a=(int(input("Primeiro número: ")))
        b=(int(input("Segundo número: ")))
        print("A multiplicação é ", a*b)
        input("Pressione ENTER para voltar ao MENU! ")
    if resposta == "4":
        a=(int(input("Primeiro número: ")))
        b=(int(input("Segundo número: ")))
        print("A divisão é ", a/b)
        input("Pressione ENTER para voltar ao MENU! ")
    if resposta == "5":
        a=(int(input("Digite o número: ")))
        if a % 2 !=0:
            print("O número é ímpar")
        else: 
            print("O número é par")
        input("Pressione ENTER para voltar ao MENU! ")
    if resposta == "6":
        a=(int(input("Digite o número: ")))
        i=1
        fatorial=1
        while i< a+1:
            fatorial*= i
            i+=1
        print("O fatorial do número é", fatorial)
        input("Pressione ENTER para voltar ao MENU! ")
    if resposta == "7":
        a=(int(input("Digite o número: ")))
        cont=0
        i=1
        while i<=a:
            if a%i==0:
                cont+=1
            i+=1
        if cont==2:
            print("O número", a, "é primo.")
        else:
            print("O número", a, "não é primo.")
        input("Pressione ENTER para voltar ao MENU! ")
    if resposta== "SAIR" or "sair" or "Sair":
        print("A sessão terminou.")
        break
print("********** OPERAÇÕES MATEMÁTICAS **********")
print("Escolha uma das operações matemáticas abaixo. Para encerrar digite 'SAIR' :")
print("1- Soma")
print("2- Subtração")
print("3- Multiplicação")
print("4- Divisão")
print("5- Par ou ímpar")
print("6- Fatorial")
print("7- Primo")
resposta= (input("Escolha qual operação matemática deseja usar, colocando o número da operação ou <SAIR> para encerrar: "))
