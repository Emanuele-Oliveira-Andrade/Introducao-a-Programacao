Thanos=1.50
Miranha=1.10
for i in range (1000):
    if Miranha>Thanos:
        break
    Thanos+=0.02
    Miranha+=0.03
print("Vai demorar", i, "anos para que o Homem Aranha seja maior que o Thanos!")
