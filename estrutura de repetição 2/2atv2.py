i = 1
cont1 = 0
cont1a4 = 0
cont5e6 = 0
cont7 = 0
cont8a15 = 0

while i != 0:
    i = int(input("Insira o código do produto:\n1 - Alimento não-perecível\n2 a 4 - Alimento perecível\n5 e 6 - Vestuário\n7 - Higiene pessoal\n8 a 15 - Limpeza e utensílios domésticos\n0 para finalizar\nCódigo: "))
    
    match i:
        case 0:
            break
        case 1:
            cont1 += 1
        case 2|3|4:
            cont1a4 += 1
        case 5|6:
            cont5e6 += 1
        case 7:
            cont7 += 1
        case 8|9|10|11|12|13|14|15:
            cont8a15 += 1
        case _:
            print("Código inválido")

print("Quantidade de cada produto: ")
print("Alimento não-perecível: ", cont1)
print("Alimento perecível: ", cont1a4)
print("Vestuário: ", cont5e6)
print("Higiene pessoal: ", cont7)
print("Limpeza e utensílios domésticos: ", cont8a15)


