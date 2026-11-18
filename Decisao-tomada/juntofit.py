'''
Na "JUNTOFIT", se um aluno tiver frequência de 21 vezes, sem interrupções, ele ganha um mês de aulas gratuitas para presentear um acompanhante. Caso contrário, ele não se qualifica para o benefício.

Na catraca de acesso, haverá uma tela voltada para o cliente. Todos os dias, quando ele passar, deve aparecer a mensagem "VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO"

Quando ele completar 21 identificações seguidas, deve aparecer a mensagem "UHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ".

Caso o cliente tenha uma certa frequência, mas falte algum dia, quando retornar, deve aparecer "QUE BOM VER VOCÊ DE VOLTA. A PARTIR DE AGORA INICIAMOS MAIS UMA CONTAGEM DE 21 DIAS PARA A PROMO TREINA JUNTO."
'''

# Usuário = Catraca

# Cada dia, deve perguntar se o aluno veio

# Cada presença soma +1 na frequencia

# Caso falte, reseta


# Caso venha após uma falta, iniciar contagem com mensagem nova


presenca = input('O aluno veio hoje? [sim/não] ').lower() # Sim, SIM, sim
frequencia = 0

# Estamos no primeiro dia

if presenca == "sim":

    faltou_ontem = input('O aluno faltou ontem? [sim/não] ').lower()

    if faltou_ontem == 'sim':
        print('QUE BOM VER VOCÊ DE VOLTA. A PARTIR DE AGORA INICIAMOS MAIS UMA CONTAGEM DE 21 DIAS PARA A PROMO TREINA JUNTO.')
        frequencia += 1 # == frequencia = frequencia + 1
    elif faltou_ontem == 'não':
        print('VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO')
        frequencia += 2 # == frequencia = frequencia + 2
    else:
        print('Não entendi o que você digitou, melhore!')
elif presenca == "não":
    print('Execute de novo amanhã!')

# ------------------------------


for frequencia in range (0, 22):
    print(f"Frequência é {frequencia}")

    presenca = input("O aluno veio hoje? ")
    if frequencia != 21:
        if presenca == "Sim":
            frequencia += 1

            print('VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO')

            print(f"A frequencia atual é {frequencia}.")
        elif presenca == "não":
            break
    elif frequencia == 21:
        print('UHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ')