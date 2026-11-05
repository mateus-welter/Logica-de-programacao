valorC = float(input("Insira o valor do carro: "))

vista = int(input("Compra à vista? 1 para sim e 0 para não: "))
if vista == 0:
    parc = int(input("Deseja comprar em quantas parcelas?\n6, 12 ,18, 24, 30, 36, 42, 48, 54 ou 60 parcelas\nQuantidade de parcelas: "))
    match parc:
        case 6:
            precoF = valorC * 1.03
        case 12:
            precoF = valorC * 1.06
        case 18:
            precoF = valorC * 1.09
        case 24:
            precoF = valorC * 1.12
        case 30:
            precoF = valorC * 1.15
        case 36:
            precoF = valorC * 1.18
        case 42:
            precoF = valorC * 1.21
        case 48:
            precoF = valorC * 1.24
        case 54:
            precoF = valorC * 1.27
        case 60:
            precoF = valorC * 1.30
    
    print("Valor final do carro é R$", precoF)
    print("Quantidade de parcelas:", parc)
    print("Preço de cada parcela:",precoF / parc)

elif vista == 1:
    print("Valor final do carro é R$", valorC * 0.8)
    print("Pago à vista, não tem parcelas")
        