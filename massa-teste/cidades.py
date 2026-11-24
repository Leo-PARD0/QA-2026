import pandas as pd

dados = {
    'Nome': ['Carlos', 'Mariana', 'Lucas', 'Fernanda', 'Rafael', 'Juliana', 'Pedro'],
    'Idade': [25,33,22,15,23,45,32],
    'Cidade': ['Recife', 'Recife', 'Recife', 'Salvador', 'Salvador', 'São Paulo', 'Manaus']
}

df = pd.DataFrame(dados) # --> "Carlos" : "Recife", "Mariana" : "Recife"

df_recife = df[df['Cidade'] == 'Recife']

print (df_recife)

