numjogadores= int(input("Digite o número de jogadores: "))
mediaaltura= 0
for i in range(numjogadores):
    altura= int(input ("Digite a altura do jogador em cm: "))
mediaaltura= (altura)+ (mediaaltura)/ numjogadores
print("A altura média dos jogadores é:", mediaaltura)