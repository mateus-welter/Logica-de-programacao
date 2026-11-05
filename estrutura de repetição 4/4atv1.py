"""
Balanceamento Dinâmico de Linha de Produção
Uma linha tem 5 estações.
Cada estação:
Recebe peças
Processa no máximo X por ciclo
Pode quebrar se operar acima de 90% da capacidade por 5 ciclos seguidos
Regras:
Peças não processadas acumulam
Se uma estação quebra:
Toda a linha para
Produção continua até:
Meta diária atingida
Ou falha estrutural
Exibir:
Produção total
Estação que falhou (se houver)
Ciclos executados
"""
metaf = False
meta = int(input("Qual a meta diária? "))
peca = int(input("Quantas peças foram recebidas? "))
cap1 = int(input("Capacidade de produção da máquina 1: "))
cap2 = int(input("Capacidade de produção da máquina 2: "))
cap3 = int(input("Capacidade de produção da máquina 3: "))
cap4 = int(input("Capacidade de produção da máquina 4: "))
cap5 = int(input("Capacidade de produção da máquina 5: "))

while metaf == False:
    if peca