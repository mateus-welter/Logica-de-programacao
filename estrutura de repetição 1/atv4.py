salario = 0
Ftotal = 0
Stotal = 0
i = 0
i100 = 0
Smaior = 0

while salario >= 0:
    filhos = int(input("Insira o número de filhos você tem: "))
    salario = int(input("Insira o seu salário (salario negativo para finalizar pesquisa): "))

    if salario >= 0:
        Ftotal += filhos
        Stotal += salario
        i += 1

    if salario > Smaior:
        Smaior = salario

    if salario <= 100 and salario >= 0:
        i100 += 1


mediaF = Ftotal / i
mediaS = Stotal / i
percentual = (i100 / i) * 100

print("A média de filhos é ", mediaF,"\nA média de salário é R$", mediaS,"\nO maior salário é R$", Smaior,"\nO percentual de pessoas com salário até R$100 é ", percentual,"%")