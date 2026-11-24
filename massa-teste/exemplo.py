'''
nome        idade
joão        52
marta       37
ary         23
matheus     24 
michele     33

'''

import pandas as pd

dados = {
    'nomes' : ['João', 'Marta', 'Ary', 'Matheus', 'Michele'],
    'idades': [52, 37, 23, 24, 33]
}

df = pd.DataFrame(dados)

print(50*'=')
print('Antes do PANDAS')
print(50*'=')

print(dados)

print(50*'=')
print('Depois do PANDAS')
print(50*'=')

print(df)