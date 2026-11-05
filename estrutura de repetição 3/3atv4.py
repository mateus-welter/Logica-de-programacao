total = 0
totalV = 0
totalP = 0

for i in range (15):
    transacao = int(input("Que tipo de transação deseja realizar?\n1 - transação á vista\n2 - transação à prazo\nTipo: "))
    valor = float(input("Insira o valor da transação: "))
    
    if transacao == 1:
        totalV += valor
        total += valor
    elif transacao == 2:
        totalP += valor
        total += valor
        print("O valor da primeira prestação é R$",valor / 3)

print("Valor total de todas as transações: R$",total)
print("Valor total das transações à vista: R$",totalV)
print("Valor total das transações à prazo: R$",totalP)