bateria= int(input("Digite o nível de bateria: "))
temperatura= int(input("Digite a temperatura do ambiente: "))
umidade= int(input("Digite a umidade do solo: "))
modo= input("Digite o modo de operação (plantio, colheita ou irrigação): ").upper()


if bateria < 20:
    print("Bateria muito baixa! Retorne imediatamente para a base.")
if bateria>=20:
    if bateria<50:
        print("Atenção: bateria em nível moderado.")
if bateria>=50:
    print("Bateria suficiente para operação.")


if temperatura>40:
    print("Temperatura crítica! Operação suspensa.")
if temperatura<5:
    print("Frio extremo! Modo de economia ativado.")


if umidade<30:
    print("Solo muito seco. Recomendado iniciar irrigação.")
if umidade>80:
    print("Solo encharcado! Suspenda irrigação imediatamente.")


if modo== "PLANTIO":
    print("Iniciando modo PLANTIO...")
if modo== "COLHEITA":
    print("Iniciando modo COLHEITA...")
if modo== "IRRIGAÇÃO":
    print("Iniciando modo IRRIGAÇÃO...")


if bateria >= 50:
    if temperatura >= 10:
        if temperatura <= 35:
            if umidade >= 30:
                if umidade <= 80:
                    print("Robô autorizado a iniciar a operação!")


if bateria < 50:
    print("Operação negada! Verifique as condições do ambiente.")
if temperatura < 10:
    print("Operação negada! Verifique as condições do ambiente.")
if temperatura > 35:
    print("Operação negada! Verifique as condições do ambiente.")
if umidade < 30:
    print("Operação negada! Verifique as condições do ambiente.")
if umidade > 80:
    print("Operação negada! Verifique as condições do ambiente.")
