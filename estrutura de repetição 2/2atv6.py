num = 1
totalN = 0
totalP = 0
nN = ""
nP = ""

while num != 0:
    num = int(input("Digite um número: "))

    if num%2 == 0 and num != 0:
        nP += str(num) + " "

    elif num != 0:
        nN += str(num) + " "
    
    if num > 0:
        totalP += num
    elif num < 0:
        totalN += num


print("Soma dos números positivos: ", totalP)
print("Soma dos números negativos: ", totalN)
print("Soma de tudo: ", totalN + totalP)
print(nP)
print(nN)