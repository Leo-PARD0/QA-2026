from faker import Faker
import pandas as pd

fake = Faker('pt_BR')

dados = {
    'Nome': [],
    'idade': [],
    'cidade': []
}

for i in range (1, 5):
    nome = fake.name()
    idade = fake.random_int(min=18, max=90)
    cidade = fake.city()

    dados['Nome'].append(nome)
    dados['idade'].append(idade)
    dados['cidade'].append(cidade)

df = pd.DataFrame(dados)

print(df)