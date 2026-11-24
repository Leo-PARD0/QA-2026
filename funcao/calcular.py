# Faça um código para formar a soma de dois números, usando o comando 'return'.

def calcular(n1, n2):
    resultado = n1 + n2

    return resultado



num1 = float(input('Digite o primeiro número da soma: '))
num2 = float(input('Digite o segundo número da soma: '))

retorno = calcular(num1, num2)

print(f'A soma de {num1} com {num2} é {retorno}')