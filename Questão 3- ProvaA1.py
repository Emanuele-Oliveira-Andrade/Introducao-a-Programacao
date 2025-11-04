print("Ana Eduarda, Byank Chrystinny, Emanuele, Guilherme.")
anterior=1
atual=1
contador=2
while contador<51: 
    proximo=anterior+atual
    anterior=atual
    atual=proximo
    contador+=1
print("O 51° termo da sequência é:", atual)