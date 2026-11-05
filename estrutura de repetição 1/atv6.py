i = int(input("Escreva um número incial para fazer a contagem regressiva: "))
inter = int(input("Escreva o intervalo entre cada contagem: "))

for n in range (i + 1):
    if not (i - (n * inter)) <= 0:
        print(i - (n * inter))
    else:
        print("0")
        break