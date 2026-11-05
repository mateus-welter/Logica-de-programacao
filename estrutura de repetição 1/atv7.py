num = 0
i = 0
total = 0

while num >= 0:
    num = int(input("Insira um número: "))

    if num >= 0:
        total += num
        i += 1

media = total / i

print("A média dos números é: ", media)