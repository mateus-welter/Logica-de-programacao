num = 1
total = 0
i = 0

while num != 0:
    num = int(input("Insira um número (0 para finalizar): "))

    if num%2 == 0 and num != 0:
        total += num
        i += 1

media = total / i

print("A média dos números pares é ", media)