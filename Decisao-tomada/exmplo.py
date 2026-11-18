hoje = int(input(" Digite a data de Hoje! "))
lançamento = False

while hoje == 18:
    lançamento = True

    if lançamento == True:
        print("Hoje lançou GTA VI")
    else:
        print("GTA VI já lançou")

    dia = input("Passou o dia?")

    if dia == 'sim':
        break