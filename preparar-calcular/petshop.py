'''
A dona de um PETSHOP quer criar um programa para calcular a idade dos cachorros de seus clientes em "anos de cachorro". Como os pets envelhecem de maneira diferente dos humanos - cada ano humano corresponde a 7 do Cachorro.
'''

# Calcular a idade do cachorro com base na idade humana

# Regras -> Para cada ano humano, o cachorro envelhece 7 anos.


# Não sabemos a idade humana, então perguntamos
idade_humana = int(input("Quantos aniversários seu cachorro fez? "))

idade_canina = idade_humana * 7

print(f"A idade canina do seu pet é: {idade_canina}")

'''
Além disso, ela deseja calcular, a cada 12 meses, o lucro obtido por banho e por cachorro. 

VALORES POR BANHO X CUSTO POR BANHO

Cachorro de grande porte: BANHO: R$75,00 | CUSTO: R$20,00
Cachorro de médio porte: BANHO: R$60,00 | CUSTO: 15,00
Cachorro de médio porte: BANHO: R$50,00 | CUSTO: R$5,00
Exemplo: Se um animal de grande porte tomar 10 banhos em 12 meses, no final, o programa deve imprimir a seguinte informação:
'''

# ________________________________________________________________________

nome = input("Qual o nome do pet? ")

print(50*"=")
print(f"Digite o VALOR referente ao porte do {nome}:")
print("Digite 75 para porte GRANDE")
print("Digite 60 para porte MÉDIO")
print("Digite 50 para porte PEQUENO")

valor = int(input())

print(50*"=")
print(f"Digite o VALOR referente ao custo por porte do {nome}:")
print("Digite 20 para porte GRANDE")
print("Digite 15 para porte MÉDIO")
print("Digite 5 para porte PEQUENO")

custo = int(input())

banhos_p_mes = int(input(f"Digite quantos banhos {nome} toma por mês? "))

valor_anual = (valor - custo) * banhos_p_mes * 12

print(f"Olá, {nome} tem {idade_canina} anos em idade de cachorro e seu lucro anual é: 💵R${float(valor_anual)}")