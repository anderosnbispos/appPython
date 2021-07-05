# By Rafael Galleani
#
# O que são pacotes
# O que eh o instalador de pacotes do Python (PIP)
# Como listar pacotes instalados no Python
# Como utilizar um pacote
# Instalar nosso primeiro pacote (Requests)
# Realizar uma requisicao http com requests

import requests

def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code)
    # print(response.json())
    # print(type(response.json()))
    dados_cep = response.json()
    print(dados_cep['bairro'])

def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_poke = response.json()
    # print(dados_poke['name'])
    return dados_poke

def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    # retorna_dados_cep('41720030')
    # dados = retorna_dados_pokemon('pikachu')
    # print(dados['sprites']['front_shiny'])
    response = retorna_response('https://digitalinnovation.one')
    print(response)