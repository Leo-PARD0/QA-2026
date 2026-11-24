# Faça o código que dê boas vindas para nomes específicos.

def bem_vindo(nome):
    print(f'Olá, {nome}! Seja bem vindo!')

bem_vindo(input('digite seu nome: '))

# -------------------

lista_de_nomes = ['Leo', 'Maria', 'Gustavo', 'Gustavo', 'Mikael', 'Caio', 'Giacomo']

for n in lista_de_nomes:
    bem_vindo(n)