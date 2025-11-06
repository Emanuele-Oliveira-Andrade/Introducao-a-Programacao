print("Guilherme Carrijo, Emanuele, Ana e Byank.")
numero= int(input("Digite um número: "))
resultado=""
resto=0
while (numero%16>0):
    resto=numero%16
    if resto==10:
        resultado="A"
    if resto==11:
        resultado="B"
    if resto==12:
        resultado="C"
    if resto==13:
        resultado="D"
    if resto==14:
        resultado="E"
    if resto==15:
        resultado=resultado+"F"
    numero=numero//16
print(resultado)

