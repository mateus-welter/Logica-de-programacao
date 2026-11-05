num = 1
i = 0

while num != 0:
    num = int(input("Insira um número: "))
    if num < 0:
        i += 1

print("Você digitou ", i," números negativos")