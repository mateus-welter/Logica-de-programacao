import random

num = random.randint(1,50)
print(num)
errou = 1

for i in range (5):
    tentar = int(input("Digite um valor: "))
    if num == tentar:
        print("Você acertou")
        errou = 0
        break
    elif num > tentar:
        print("Tente novamente, seu número é menor que o certo")
    elif num < tentar:
        print("Tente novamente, seu número é maior que o certo")

if errou == 1:
    print("O número era: ", num,"\nVocê perdeu")
