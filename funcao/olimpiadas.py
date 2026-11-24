'''
Uma escola está organizando sua primeira olimpíada do conhecimento e deseja separar os 100 alunos em dois grupos de 50. Além de testar os conhecimentos dos alunos, querem estimular a formação de novos laços sociais e, por isso, a divisão dos grupos de alunos será feita seguindo um critério:

Alunos com número de matrícula par, ficarão no grupo azul.
Alunos com número de matrícula ímpar, ficarão no grupo amarelo. 
Os alunos ainda não sabem dessa regra de separação dos grupos e, no dia do evento, quando digitarem o número da matrícula na catraca, deve aparecer no painel a cor do grupo que ele deve integrar. 

DESAFIO: Desenvolvam uma função para retornar se o número passado pelo usuario no console é par ou ímpar.

Caso o número de matrícula do(a) aluno(a) seja par imprima:
VOCÊ ESTÁ NO TIME AZUL

Caso o número de matrícula do(a) aluno(a) seja impar imprima:
VOCÊ ESTÁ NO TIME AMARELO
'''

'''
Agora, criem um scritp para:

Ter um input de usuário para inserir os números de matrícula em uma lista. 

Ter um validador nessa lista que permita a inserção de dados até ocupar 5 espaços index.

Fazer um laço de repetição para passar todos os números da lista em uma função para verificar se o número é par ou ímpar. 
'''

# usuário = catraca

def time(matricula):
    if matricula % 2 == 0:
        return f'{matricula} ESTÁ NO TIME AZUL💙'
    else:
        return f'{matricula} ESTÁ NO TIME AMARELO💛'

matriculas = []

for n in range(1,6):
    num_matricula = int(input('Digite o número da sua matricula: '))

    matriculas.append(num_matricula)

    print(matriculas)

for num in matriculas:
    retorno = time(num)
    print(retorno)