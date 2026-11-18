'''
Em SQUADs

Mini Case 1: Idade do Pet e Lucro do PETSHOP

A dona de um PETSHOP quer criar um programa para calcular a idade dos cachorros de seus clientes em "anos de cachorro". Como os pets envelhecem de maneira diferente dos humanos - cada ano humano corresponde a 7 do Cachorro.

Desafio: Crie um programa Python que calcule a idade de cachorro com base na idade humana.

O que seu programa deve conter:

Solicitar ao usuário a idade humana do pet (um número inteiro).
Calcular a idade do pet, levando em consideração que cada ano da idade humana corresponde a 7.
Exibir a idade do pet ao usuário.
Além disso, ela deseja calcular, a cada 12 meses, o lucro obtido por banho e por cachorro. 

VALORES POR BANHO X CUSTO POR BANHO

Cachorro de grande porte: BANHO: R$75,00 | CUSTO: R$20,00
Cachorro de médio porte: BANHO: R$60,00 | CUSTO: 15,00
Cachorro de pequeno porte: BANHO: R$50,00 | CUSTO: R$5,00
Exemplo: Se um animal de grande porte tomar 10 banhos em 12 meses, no final, o programa deve imprimir a seguinte informação:

Olá, Tuco tem 35 anos e nos últimos 12 meses o lucro com este animal foi de R$550,00
'''


# Usuário = Dona do petshop

# Ano de cachorro = Ano * 7

nome = input("Digite o nome do pet: ")
idade = int(input("Quantos anos o pet tem? "))

ano = idade * 7

print(50*"_")

print("Digite o valor referente ao porte do pet!")

print("Grande porte ____ 75")
print("Médio porte ____ 60")
print("Pequeno porte ____ 50")

valor_p_banho = int(input(""))

print(50*"_")

print("Digite o custo referente ao porte do pet!")

print("Grande porte ____ 20")
print("Médio porte ____ 15")
print("Pequeno porte ____ 05")

custo_p_banho = int(input(""))

lucro_p_banho = valor_p_banho - custo_p_banho

quantidade_banhos_ano = int(input("Quantos banhos o pet toma por ano: "))

lucro_total = lucro_p_banho * quantidade_banhos_ano

print(50*"_")

print(f"Olá, {nome} tem {ano} anos e gera um lucro de R$ {lucro_total} a cada 12 meses")

# Olá, Tuco tem 35 anos e nos últimos 12 meses o lucro com este animal foi de R$550,00