from faker import Faker
import pandas as pd

fake = Faker('pt_BR')

dados = {
    'Nome': [],
    'idade': []
}

for i in range (1, 26):
    nome = fake.name()
    idade = fake.random_int(min=18, max=90)

    dados['Nome'].append(nome)
    dados['idade'].append(idade)

print(dados)

print(50*'-')

df = pd.DataFrame(dados)

print(df)