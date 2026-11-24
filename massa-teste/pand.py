import pandas as pd 

dados = {
    'nomes' : ['João', 'Marta', 'Ary', 'Matheus', 'Michele'],
    'idades' : [51, 37, 23, 24, 33]
}

print(50*'=')
print("Antes do Data frame")
print(50*'=')

print()

print(dados)

print()

print(50*'=')
print("Com Data frame")
print(50*'=')

print()

df = pd.DataFrame(dados)

print(df)