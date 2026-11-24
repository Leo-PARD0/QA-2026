'''
Desenvolvam um programa que conte quantas vogais (a, e, i, o, u) existem em uma palavra fornecida pelo usuário.

Implementem uma função que receba uma palavra qualquer (string) como entrada.
O programa deve imprimir o número total de vogais na palavra.
Solicitação de Entrada:

Implementem a solicitação de entrada de uma palavra (string).
Contagem de Vogais:

Implemente um loop "for" ou "while" para percorrer cada caractere da palavra.
Verifique se cada caractere é uma vogal (a, e, i, o, u) e conte-as.
Imprima o número total de vogais na palavra.
'''

# usuário: geral

palavra = input('Digite uma palavra: ').lower().strip() # paralelepípedo

vogais = ['a', 'e', 'i', 'o', 'u']

contar = 0

for letra in palavra:

    if letra in "aeiou":


    '''for l in vogais:
        if l == letra:
            print (f'{letra} é uma vogal')
            contar += 1
            break'''

print(f'A quantidade de vogais é: {contar}')


# A != a  á != a