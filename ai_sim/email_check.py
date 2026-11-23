'''
O instituto Joga Junto vai checar todos os emails existentes utilizados pelos usuários. Para isso sua equipe precisará criar  um código para verificar se o email inserido pelo usuário tem o @jogajuntoinstituto.org no texto. 

Crie um input para verificar esse texto.

Crie casos de teste escritos em BDD, um com sucesso, e outro com falha. Execute os testes, documente e suba os resultados no Bitrix da sua equipe. 
'''


email = input("Insira o email: ")

if "@jogajuntoinstituto.org" in email:
    passou = True
    print(f"O email {email} POSSUI o domínio do joga junto.")
else:
    passou = False
    print(f"O email {email} NÃO possui o domínio do joga junto.")

