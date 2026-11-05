"""
Uma loja tem 150 clientes cadastrados e deseja mandar uma 
correspondência a cada um deles anunciando um bônus especial. Escreva 
um algoritmo que leia o nome do cliente e o valor das suas compras no ano 
passado e calcule um bônus de 10% se o valor das compras for menor que 
500.000 e de 15 %, caso contrário. 
"""
nome = input("Digite o seu nome: ")
valor = float(input("Insira o valor das suas compras no ano passado: "))

if valor < 500000:
    bonus = valor * 0.1
    print(nome,"recebeu um bônus de R$",bonus)
else:
    bonus = valor * 0.15
    print(nome,"recebeu um bônus de R$",bonus)