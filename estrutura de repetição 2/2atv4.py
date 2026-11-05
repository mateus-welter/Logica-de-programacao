p1 = 0
p2 = 0
fim = False

while fim != True:
    cod = int(input("Jogador 1 ou 2 venceu? "))

    match cod:
        case 1:
            p1 += 1
        case 2:
            p2 += 1

    dif1 = p1 - p2
    dif2 = p2 - p1

    if p1 >= 21 and dif1 >= 2:
        fim = True
        print("Jogador 1 venceu")
    elif p2 >= 21 and dif2 >= 2:
        fim = True
        print("Jogador 2 venceu")