num = int(input("Insira o numero que deseja saber a tabuada: "))
tabuada = int(input("Deseja saber a tabuada deste número até quanto? "))

for i in range (tabuada):
    print(num ,"*", i + 1 ,"=", num * (i + 1))