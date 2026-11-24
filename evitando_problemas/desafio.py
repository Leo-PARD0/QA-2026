'''
Vamos explorar o poder das requisições e da biblioteca OS! Prepare-se para mergulhar no mundo das APIs e da interação entre o Python e o seu sistema operacional. Vamos aprender a usar o requests e a biblioteca OS em conjunto com funções nativas do Python para criar algo.
O desafio é o seguinte: faça um ambiente virtual, instale o requests e faça o código com os seguintes requisitos:
* Tenha uma estrutura de dicionário com nome e cep de cada integrante. Essa estrutura deverá ser salva em uma variável apenas.
* Faça uma requisição e imprima o nome e a cidade de cada integrante do squad.
* Usando a biblioteca OS, interaja com o seu sistema operacional criando uma nova pasta para salvar um arquivo de texto txt com os dados (nome e cidade) de cada integrante.
* Gere um arquivo chamado requirements.txt que contenha todas as dependências do seu projeto.
* Ao final, suba a atividade em seu github. {O arquivo .txt tem que estar na lista negra do .gitignore}
'''

import os
import requests

squad = {
    "leo" : "11631454"
}

nome_pasta = 'dados_squad'

os.makedirs(nome_pasta, exist_ok=True)

caminho_arquivo = os.path.join(nome_pasta, "integrantes.txt")

with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
    for nome, cep in squad.items():
        url = f'https://viacep.com.br/ws/{cep}/json/'
        resposta = requests.get(url)

        if resposta.status_code == 200:

            dados = resposta.json()

            if "erro" not in dados:
                cidade = dados["localidade"]
                linha = f"Nome: {nome} | Cidade: {cidade}"

                print(linha)
                arquivo.write(linha + "\n")
            else:
                print(f"CEP inválido para {nome}.")
        else:
            print(f"Erro na requisição para {nome}. Status: {resposta.status_code}")
    
print(f"\n Arquivo salvo com sucesso em: {caminho_arquivo}")
