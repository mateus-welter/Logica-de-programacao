qtdn = 0

for i in range (80):
    num = int(input("Insira um número: "))
    if num >= 10 and num <= 150:
        qtdn += 1

print(qtdn,"número(s) entre 10 e 150")