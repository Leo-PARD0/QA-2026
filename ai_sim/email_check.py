'''
O instituto Joga Junto vai checar todos os emails existentes utilizados pelos usuários. Para isso sua equipe precisará criar  um código para verificar se o email inserido pelo usuário tem o @jogajuntoinstituto.org no texto. 

Crie um input para verificar esse texto.

Crie casos de teste escritos em BDD, um com sucesso, e outro com falha. Execute os testes, documente e suba os resultados no Bitrix da sua equipe. 
'''

# usuário: diretoria do instituto

email = input("Digite seu email: ")

if "@jogajuntoinstituto.org" in email:
    print(f'O email: {email} é do domínio @jogajuntoinstituto.org')
else:
    print(f'O email: {email} NÃO pertence ao domínio @jogajuntoinstituto.org')


'''

Dado que - contexto
Quando - ação
Então - consequência


Dado que o usuário digita 757575eze@jogajuntoinstituto.org
quando executa o código
então o sitema retorna 'O email: {email} é do domínio @jogajuntoinstituto.org'

Dado que o usuário digita 757575eze@gmail.com
quando executa o código
então O email: {email} NÃO pertence ao domínio @jogajuntoinstituto.org

'''