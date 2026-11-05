"""
Controle de Temperatura de Forno
Um forno industrial inicia com temperatura informada pelo usuário.
A cada ciclo:
Se temperatura < 800 → aumenta 50 graus
Se temperatura ≥ 800 e < 1000 → aumenta 20 graus
Se temperatura ≥ 1000 → mantém constante
O sistema deve repetir até:
Atingir 1000 graus
Exibir:
Quantos ciclos foram necessários
Temperatura final
"""
ciclo = 0

temp = float(input("Temperatura inicial do forno industrial: "))

while temp < 1000:
    if temp < 800:
        temp += 50
    elif temp >= 800 and temp < 1000:
        temp += 20
    
    ciclo += 1

print(f"Foram necessários {ciclo} ciclos para a temperatura atingir 1000 graus")
print(f"Temperatura final: {temp}ºC")