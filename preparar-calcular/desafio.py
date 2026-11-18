'''
•Crie uma tupla com 5 dados

•Altere a tupla para uma lista

•Insira 2 dados extras a essa lista

•Remova o primeiro dado da lista

•Remova o último dado da lista

•Faça um print com o primeiro dado da lista

•Faça um print com a quantidade de dados da lista

•Crie um dicionário com os seguintes dados:
Nome, Idade, Profissão

•Imprima somente o valor contido na chave Nome do dicionário
'''

frutas = ("Maçã" , "Banana", "Melancia" , "Morango" , "Abacaxi")

frutas_lista = list(frutas)
print(frutas_lista)

# .append() - Adicionar 1 elemento por vez

# frutas_lista.append("Tomate")

# .extend() - Juntar duas listas

frutas_lista.extend(["Tomate", "Laranja"])

print(frutas_lista)

# .pop() - remove um ítem (indicado pelo índice) da lista

frutas_lista.pop(0)
print(frutas_lista)

tamanho = len(frutas_lista)

print(tamanho)

frutas_lista.pop(tamanho-1)

print(frutas_lista)

print(frutas_lista[0])
print(len(frutas_lista))

print(20*"-")

# ----------------

dados = {
    "nome" : input("Digite seu nome: "),
    "idade" : input("Digite sua idade: "),
    "profissão" : input("Digite sua profissão: ")
}

print(dados["nome"])