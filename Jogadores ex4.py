numjogadores= int(input("Digite o número de jogadores: "))
soma_alturas= 0
for i in range(numjogadores):
    altura= int(input ("Digite a altura do jogador em cm: "))
    soma_alturas+= altura
mediaaltura= (soma_alturas)/ numjogadores
print("A altura média dos jogadores é:", mediaaltura)