'''
Na "FashionStyle", para um cliente obter 10% de desconto em suas compras, a compra deve ser de pelo menos R$250,00 e para obter 30%, a compra deve ser acima de R$500,00. Caso contrário, nenhum desconto é aplicado.

No caixa, haverá uma tela voltada para o cliente. Ao passar o produto, caso cumpra o requisito da promoção, aparecerá a mensagem:

Caso o cliente não cumpra o requisito, deve aparecer "POXA, FALTA POUCO PARA VOCÊ GANHAR 10% DE DESCONTO EM SUA COMPRA."

Caso o cliente faça uma compra acima de R$250,00 "PARABÉNS. VOCÊ GANHOU 10% DE DESCONTO, MAS PODE GANHAR 30% SE SUA COMPRA FOR ACIMA DE R$500,00"

Caso o cliente faça uma compra acima de R$500,00 "PARABÉNS. VOCÊ GANHOU SUPER DESCONTO DE 30%"
'''

# usuário = caixa da loja

valor = 0

while True:

    valor += int(input("Digite o valor do produto: "))

    if valor < 250:
        desconto = 0
        print('💵Valor💵')
        print(valor)

        falta = 250 - valor

        print(f'POXA, FALTA R${falta} PARA VOCÊ GANHAR 10% DE DESCONTO EM SUA COMPRA.')
    elif valor >= 250 and valor < 500:
        desconto = 10
        print('💵Valor💵')
        print(valor)
        print(f'PARABÉNS. VOCÊ GANHOU {desconto}% DE DESCONTO, MAS PODE GANHAR 30% SE SUA COMPRA FOR ACIMA DE R$500,00')
    elif valor >= 500:
        desconto = 10
        print('💵Valor💵')
        print(valor)
        print(f'PARABÉNS. VOCÊ GANHOU SUPER DESCONTO DE 30%')
    else:
        print('❌Deu algum erro na conta❌')

    fechar = input('ÚLTIMO ÍTEM? [Pressione enter para continuar]')

    if fechar != '':
        break
