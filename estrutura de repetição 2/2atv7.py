cont4 = 0
cont5 = 0
cont7 = 0
cont12 = 0
totalpessoas = 0
canal = 1

while canal != 0:
    canal = int(input("\nQual o número do canal?\n4, 5, 7 ou 12\n0 para finalizar pesquisa\nCanal: "))
    if canal != 0:
        pessoas = int(input("Quantas pessoas estão assistindo? "))

        match canal:
            case 0:
                 break
            case 4:
                cont4 += pessoas
            case 5:
                cont5 += pessoas
            case 7:
               cont7 += pessoas
            case 12:
                cont12 += pessoas
            case _:
                print("Canal inválido")

totalpessoas = cont12 + cont4 + cont5 + cont7

porcentagem4 = (cont4 / totalpessoas) * 100
porcentagem5 = (cont5 / totalpessoas) * 100
porcentagem7 = (cont7 / totalpessoas) * 100
porcentagem12 = (cont12 / totalpessoas) * 100

print(totalpessoas ,"pessoas estavam assistindo")
print("Audiência no canal 4:",porcentagem4,"%")
print("Audiência no canal 5:",porcentagem5,"%")
print("Audiência no canal 7:",porcentagem7,"%")
print("Audiência no canal 12:",porcentagem12,"%")
