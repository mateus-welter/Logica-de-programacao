contH = 0
contM = 0

for i in range (56):
    nome = input("Digite seu nome: ")
    sexo = int(input("Insira seu sexo:\n1 para homem e 0 para mulher\nsexo: "))

    if sexo == 1:
        contH += 1
        print(nome,"é homem")
    elif sexo == 0:
        contM += 1
        print(nome,"é mulher")

print("Quantidade de homens:", contH)
print("Quantidade de mulheres:", contM)