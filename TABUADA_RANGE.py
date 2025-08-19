print("Esta aplicação mostra a tabuada de 1 a 10 de um número digitado!")
numero=int(input("Digite um número: "))
for i in range(10):
    print(numero, "x", i+1, "=", numero*(i+1))