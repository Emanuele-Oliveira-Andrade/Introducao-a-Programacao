print("Guilherme Carrijo, Emanuele, Ana e Byank.")
print("Escreva um algoritmo que calcule a soma de todos os múltiplos de 7 entre 1 e 200.")
soma = 0
for i in range (1, 200):
    if i % 7 == 0:
        soma+=i
print("O resultado de todos os múltiplos de 7 de 1 a 200 é" , soma)