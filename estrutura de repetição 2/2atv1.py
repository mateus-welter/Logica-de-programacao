ncarroTotal = 0
acidentemaior = -1
acidentemenor = float('inf')
nomeMaior = ""
nomeMenor = ""
est = ""
cid = ""
estMai = ""
estMen = ""
sCTotal = 0
rSTotal = 0
pRTotal = 0

for i in range(12):
    codeCid = int(input("Insira o código da cidade: "))
    nCarroP = int(input("Insira a quantidade de veículos de passeio na cidade: "))
    nacidente = int(input("Insira o número de acidentes com vítimas que ocorreu: "))

    match codeCid:
        case 11:
            cid = "Jaraguá do Sul"
            est = "SC"
        case 12:
            cid = "Joinville"
            est = "SC"
        case 13:
            cid = "Blumenau"
            est = "SC"
        case 14:
            cid = "Florianópolis"
            est = "SC"
        case 21:
            cid = "Porto Alegre"
            est = "RS"
        case 22:
            cid = "Bento Gonçalves"
            est = "RS"
        case 23:
            cid = "Garibaldi"
            est = "RS"
        case 24:
            cid = "Caxias do Sul"
            est = "RS"
        case 31:
            cid = "Curitiba"
            est = "PR"
        case 32:
            cid = "Foz do Iguaçu"
            est = "PR"
        case 33:
            cid = "Toledo"
            est = "PR"
        case 34:
            cid = "Cascavel"
            est = "PR"
    
    if nacidente > acidentemaior:
        nomeMaior = cid
        estMai = est
        acidentemaior = nacidente
    
    if nacidente < acidentemenor:
        nomeMenor = cid
        estMen = est
        acidentemenor = nacidente

    ncarroTotal += nCarroP

    if est == "SC":
        sCTotal += nacidente
    elif est == "RS":
        rSTotal += nacidente
    else:
        pRTotal += nacidente

mediaSC = sCTotal / 4

print("O maior indice de acidentes foi ", acidentemaior ," acidentes na cidade de ", nomeMaior ," que fica no estado ", estMai)
print("O menor indice de acidentes foi ", acidentemenor ," acidentes na cidade de ", nomeMenor ," que fica no estado ", estMen)
print("A média de veículos nas cidades brasileiras é ", ncarroTotal/12 ," carros por cidade e média de veículos por estado é ", ncarroTotal/3," carros por estado")
print("A média de acidentes em SC é ", mediaSC," por cidade, o total de acidentes em RS é ", rSTotal, " e o total de acidentes PR é", pRTotal)