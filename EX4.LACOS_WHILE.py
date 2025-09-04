numjogadores= int(input("Digite o número de jogadores: "))
soma_alturas= 0
i=0
while i< numjogadores:
    if i< numjogadores:
        altura= int(input ("Digite a altura do jogador em cm: "))
    soma_alturas+= altura
    i+=1
mediaaltura= (soma_alturas)/ numjogadores
print("A altura média dos jogadores é:", mediaaltura)