"""
Máquina com Desgaste Acumulativo
Uma máquina começa com desgaste 0.
A cada ciclo:
Desgaste aumenta 7 unidades
Se operar acima de 70 ciclos, desgaste aumenta 10 por ciclo
Se desgaste ≥ 500 → máquina quebra
Simular até quebrar.
Exibir:
Quantos ciclos durou
Desgaste final
"""
desgaste = 0
ciclo = 0

while desgaste < 500:
    ciclo += 1
    
    if ciclo <= 70:
        desgaste += 7
    elif ciclo > 70:
        desgaste += 10

print(f"A máquina quebrou após {ciclo} ciclos")
print(f"Desgaste final: {desgaste}")